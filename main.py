from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.generator.html_generator import Generator

markdown = """
**bold with *italics inside* it**
```python
print("hello chat")
```
"""
lexer = Lexer(markdown)
tokens = lexer.get_tokens()
print(tokens)

parser = Parser(tokens)
tree = parser.parse()
parser.dump(tree)

generator = Generator(tree)
html = generator.generate()
print(html)