from pathlib import Path

from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.generator.html_generator import Generator

def build(posts_dir: Path):
    for md_file in posts_dir.glob("*.md"):
        text = md_file.read_text()
        tokens = Lexer(text).get_tokens()
        tree = Parser(tokens).parse()
        html = Generator(tree).generate()
        md_file.with_suffix(".html").write_text(html)
        yield f"Built {md_file.stem}.html"