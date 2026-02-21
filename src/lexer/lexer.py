from src.lexer.token_types import *
from src.lexer.token import Token

class Lexer:
    def __init__(self, markdown):
        self.text = markdown
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
    
    def advance(self):
        self.pos += 1
        
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char in " \t":
            self.advance()
    
    def peek(self):
        if self.pos + 1 < len(self.text):
            return self.text[self.pos + 1]
        return None
    
    def peek_at(self, offset):
        idx = self.pos + offset
        if idx < len(self.text):
            return self.text[idx]
        return None
    
    def read_line(self):
        content = ""
        while self.current_char and self.current_char != "\n":
            content += self.current_char
            self.advance()
        return content
    
    def header(self):
        level = 0
        while self.current_char and self.current_char == "#":
            level += 1
            self.advance()
        
        self.skip_whitespace()
        
        content = self.read_line()
        return Token(
            type=TokenType.HEADER,
            level=level,
            content=content
        )
    
    def list_item(self):
        self.advance()
        self.skip_whitespace()
        content = self.read_line()
        return Token(
            type=TokenType.LIST_ITEM,
            content=content
        )
    
    def ordered_list_item(self):
        while self.current_char and self.current_char.isdigit():
            self.advance()
        self.advance
        self.skip_whitespace()
        content = self.read_line()
        return Token(
            type=TokenType.ORDERED_LIST_ITEM,
            content=content
        )
    
    def blockquote(self):
        self.advance()
        self.skip_whitespace()
        content = self.read_line()
        return Token(
            type=TokenType.BLOCKQUOTE,
            content=content
        )
    
    def code_block(self):
        for _ in range(3):
            self.advance()

        language = self.read_line()
        if self.current_char == "\n":
            self.advance()
        
        code_lines = []
        while self.current_char is not None:
            if self.text[self.pos:self.pos + 3] == "```":
                for _ in range(3):
                    self.advance()
                self.read_line()
                break
        
            code_lines.append(self.read_line())
            
            if self.current_char == "\n":
                self.advance()
        
        return Token(
            type=TokenType.CODE_BLOCK,
            content={
                "language": language.strip(),
                "code": "\n".join(code_lines)
            }
        )
    
    # here lay even more dragons than ive ever seen in my life...
    def is_ordered_list_item(self):
        # check if current pos looks like "1. " or "12. " etc.
        j = self.pos
        if not self.text[j].isdigit():
            return False
        while j < len(self.text) and self.text[j].isdigit():
            j += 1
        if j < len(self.text) and self.text[j] == "." and j + 1 < len(self.text) and self.text[j + 1] == " ":
            return True
        return False
    
    def get_tokens(self):
        tokens = []
        
        while self.current_char is not None:
            if self.current_char == "\n":
                self.advance()
                
                if self.current_char == "\n":
                    tokens.append(Token(
                        type=TokenType.BLANK_LINE
                    ))

                    while self.current_char == "\n":
                        self.advance()
                
                continue
            
            if self.current_char in " \t": # spaces / tabs
                self.skip_whitespace()
                continue
            
            if self.current_char == "#":
                tokens.append(self.header())
                continue
            
            if self.current_char in ("-", "*") and self.peek() == " ":
                tokens.append(self.list_item())
                continue
            
            if self.is_ordered_list_item():
                tokens.append(self.ordered_list_item())
                continue
            
            if self.current_char == ">":
                tokens.append(self.blockquote())
                continue
            
            if self.text[self.pos:self.pos + 3] == "```":
                tokens.append(self.code_block())
                continue
            
            content = self.read_line()
            if content:
                tokens.append(Token(
                    type=TokenType.TEXT,
                    content=content
                ))
        
        tokens.append(Token(TokenType.EOF))
        return tokens