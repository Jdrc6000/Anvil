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
    
    def header(self):
        level = 0
        while self.current_char and self.current_char == "#":
            level += 1
            self.advance()
        
        self.skip_whitespace()
        
        content = ""
        while self.current_char and self.current_char != "\n":
            content += self.current_char
            self.advance()
        
        return Token(
            type=TokenType.HEADER,
            level=level,
            content=content
        )
    
    def bold(self):
        if self.current_char == "*" and self.peek() == "*":
            self.advance()
            self.advance()
        
        content = ""
        while self.current_char and not (self.current_char == "*" and self.peek() == "*"):
            content += self.current_char
            self.advance()
        
        if self.current_char == "*" and self.peek() == "*":
            self.advance()
            self.advance()
        
        return Token(
            type=TokenType.BOLD,
            content=content
        )
    
    def italic(self):
        self.advance()
        
        content = ""
        while self.current_char and self.current_char != "*":
            content += self.current_char
            self.advance()
        
        if self.current_char == "*":
            self.advance()
        
        return Token(
            type=TokenType.ITALIC,
            content=content
        )
    
    def get_tokens(self):
        tokens = []
        
        while self.current_char is not None:
            if self.current_char == "#":
                tokens.append(self.header())
            
            elif self.current_char == "*" and self.peek() == "*":
                tokens.append(self.bold())
            
            elif self.current_char == "*":
                tokens.append(self.italic())
            
            elif self.current_char == "\n":
                self.advance()
                continue
            
            elif self.current_char.isspace():
                self.skip_whitespace()
            
            else:
                content = ""
                while self.current_char and self.current_char not in "#*\n":
                    content += self.current_char
                    self.advance()
                
                if content:
                    tokens.append(Token(type=TokenType.TEXT, content=content))
        
        return tokens