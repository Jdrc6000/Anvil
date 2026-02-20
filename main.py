from src.lexer.lexer import Lexer

markdown = """
# hello
## hello level 2
"""
lexer = Lexer(markdown)
print(lexer.get_tokens())