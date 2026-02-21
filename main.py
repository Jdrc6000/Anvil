from src.lexer.lexer import Lexer
from src.parser.parser import Parser

markdown = """
*hello*
**hello**
"""
lexer = Lexer(markdown)
tokens = lexer.get_tokens()
print(tokens)

parser = Parser(tokens)
tree = parser.parse()
parser.dump(tree)