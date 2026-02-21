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
            # dont really know what to do with this...
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
        
        return Document(
            children=body
        )
    
    def statement(self):
        token_type = self.current_token.type
        
        if token_type == TokenType.HEADER:
            return self.parse_header()
        
        elif token_type == TokenType.BOLD:
            return self.parse_bold()
        
        elif token_type == TokenType.ITALIC:
            return self.parse_italic()
        
        elif token_type == TokenType.TEXT:
            return self.parse_text()
        
        else:
            self.advance()
            return None
    
    def parse_header(self):
        token = self.current_token
        self.advance()
        return Heading(
            level=token.level,
            content=token.content
        )
    
    def parse_bold(self):
        token = self.current_token
        self.advance()
        return Bold(
            content=token.content
        )
    
    def parse_italic(self):
        token = self.current_token
        self.advance()
        return Italic(
            content=token.content
        )
    
    def parse_text(self):
        token = self.current_token
        self.advance()
        return Paragraph(
            content=token.content
        )
    
    def dump(self, node, indent=0):
        pad = "  " * indent
        
        if isinstance(node, Document):
            print(f"{pad}Document")
            for child in node.children:
                self.dump(child, indent + 1)
        
        elif isinstance(node, Heading):
            print(f"{pad}Heading")
            self.dump(node.level, indent + 1)
            self.dump(node.content, indent + 1)
        
        elif isinstance(node, Bold):
            print(f"{pad}Bold")
            self.dump(node.content, indent + 1)
        
        elif isinstance(node, Italic):
            print(f"{pad}Italic")
            self.dump(node.content, indent + 1)
        
        elif isinstance(node, Paragraph):
            print(f"{pad}Paragraph")
            self.dump(node.content, indent + 1)
        
        elif isinstance(node, str):
            print(f"{pad}{node}")
        
        else:
            print(f"{pad}UNK ({node.__class__.__name__})")