from src.lexer.token import Token
from src.lexer.token_types import *
from src.parser.ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if tokens else Token(TokenType.EOF)
    
    def advance(self):
        self.pos += 1
        
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(TokenType.EOF)
    
    def peek(self):
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return None
    
    def parse(self):
        body = []
        
        while self.current_token.type != TokenType.EOF:
            node = self.statement()
            if node:
                body.append(node)
        
        return Document(children=body)
    
    def statement(self):
        token_type = self.current_token.type
        if token_type == TokenType.HEADER:
            return self.parse_header()
        
        elif token_type == TokenType.TEXT:
            return self.parse_paragraph()
        
        elif token_type == TokenType.LIST_ITEM:
            return self.parse_list()
        
        elif token_type == TokenType.ORDERED_LIST_ITEM:
            return self.parse_ordered_list()
        
        elif token_type == TokenType.BLOCKQUOTE:
            return self.parse_blockquote()
        
        elif token_type == TokenType.CODE_BLOCK:
            return self.parse_code_block()
        
        elif token_type == TokenType.BLANK_LINE:
            self.advance()
            return None
        
        else:
            self.advance()
            return None
    
    def parse_header(self):
        token = self.current_token
        self.advance()
        return Heading(
            level=token.level,
            children=self.parse_inline(token.content)
        )
    
    def parse_paragraph(self):
        lines = []
        while self.current_token.type == TokenType.TEXT:
            lines.append(self.current_token.content)
            self.advance()
        combined = "  ".join(lines)
        return Paragraph(children=self.parse_inline(combined))
    
    def parse_list(self):
        items = []
        while self.current_token.type == TokenType.LIST_ITEM:
            content = self.current_token.content
            self.advance()
            items.append(ListItem(children=self.parse_inline(content)))
        return List(items=items)

    def parse_ordered_list(self):
        items = []
        while self.current_token.type == TokenType.ORDERED_LIST_ITEM:
            content = self.current_token.content
            self.advance()
            items.append(OrderedListItem(children=self.parse_inline(content)))
        return OrderedList(items=items)

    def parse_blockquote(self):
        lines = []
        while self.current_token.type == TokenType.BLOCKQUOTE:
            lines.append(self.current_token.content)
            self.advance()
        combined = "  ".join(lines)
        return Blockquote(children=self.parse_inline(combined))
    
    def parse_code_block(self):
        token = self.current_token
        self.advance()
        return CodeBlock(language=token.content["language"], code=token.content["code"])
    
    # i mean, what even bro
    def parse_inline(self, text):
        nodes = []
        i = 0
        length = len(text)

        while i < length:
            # Image: ![alt](src)
            if text[i] == "!" and i + 1 < length and text[i + 1] == "[":
                end_bracket = text.find("]", i + 2)
                if end_bracket != -1 and end_bracket + 1 < length and text[end_bracket + 1] == "(":
                    end_paren = text.find(")", end_bracket + 2)
                    if end_paren != -1:
                        alt = text[i + 2:end_bracket]
                        src = text[end_bracket + 2:end_paren]
                        nodes.append(Image(alt=alt, src=src))
                        i = end_paren + 1
                        continue

            # Link: [text](url)
            if text[i] == "[":
                end_bracket = text.find("]", i + 1)
                if end_bracket != -1 and end_bracket + 1 < length and text[end_bracket + 1] == "(":
                    end_paren = text.find(")", end_bracket + 2)
                    if end_paren != -1:
                        link_text = text[i + 1:end_bracket]
                        url = text[end_bracket + 2:end_paren]
                        nodes.append(Link(text=link_text, url=url))
                        i = end_paren + 1
                        continue

            # Inline code: `code`
            if text[i] == "`":
                end = text.find("`", i + 1)
                if end != -1:
                    nodes.append(InlineCode(value=text[i + 1:end]))
                    i = end + 1
                    continue

            # Bold: **text**
            if text[i:i + 2] == "**":
                end = text.find("**", i + 2)
                if end != -1:
                    content = text[i + 2:end]
                    nodes.append(Bold(children=self.parse_inline(content)))
                    i = end + 2
                    continue

            # Italic: *text*
            if text[i] == "*":
                end = text.find("*", i + 1)
                if end != -1:
                    content = text[i + 1:end]
                    nodes.append(Italic(children=self.parse_inline(content)))
                    i = end + 1
                    continue

            # Plain text — collect until next special char
            start = i
            while i < length and text[i] not in ("*", "`", "[", "!"):
                i += 1
            if i > start:
                nodes.append(Text(value=text[start:i]))

        return nodes
    
    def dump(self, node, indent=0):
        pad = "  " * indent
        
        if isinstance(node, Document):
            print(f"{pad}Document")
            for child in node.children:
                self.dump(child, indent + 1)
        
        elif isinstance(node, Heading):
            print(f"{pad}Heading (level={node.level})")
            for child in node.children:
                self.dump(child, indent + 1)

        elif isinstance(node, Bold):
            print(f"{pad}Bold")
            for child in node.children:
                self.dump(child, indent + 1)

        elif isinstance(node, Italic):
            print(f"{pad}Italic")
            for child in node.children:
                self.dump(child, indent + 1)
        
        elif isinstance(node, Paragraph):
            print(f"{pad}Paragraph")
            for child in node.children:
                self.dump(child, indent + 1)
        
        elif isinstance(node, CodeBlock):
            print(f"{pad}CodeBlock (lang={node.language})")
        
        elif isinstance(node, Blockquote):
            print(f"{pad}Blockquote")
            for child in node.children:
                self.dump(child, indent + 1)
        
        elif isinstance(node, OrderedList):
            print(f"{pad}OrderedList")
            for item in node.items:
                self.dump(item, indent + 1)
        
        elif isinstance(node, OrderedListItem):
            print(f"{pad}OrderedListItem")
            for child in node.children:
                self.dump(child, indent + 1)

        elif isinstance(node, Text):
            print(f"{pad}Text: {node.value}")
        
        else:
            print(f"{pad}UNK ({node.__class__.__name__})")