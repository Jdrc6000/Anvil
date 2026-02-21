from src.parser.ast_nodes import *

class Generator:
    def __init__(self, tree):
        self.tree = tree

    def generate(self, node=None):
        if node is None:
            node = self.tree

        if isinstance(node, Document):
            return "".join(self.generate(child) for child in node.children)

        elif isinstance(node, Heading):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<h{node.level}>{inner}</h{node.level}>"

        elif isinstance(node, Paragraph):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<p>{inner}</p>"

        elif isinstance(node, Bold):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<strong>{inner}</strong>"

        elif isinstance(node, Italic):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<em>{inner}</em>"

        elif isinstance(node, Text):
            return node.value

        else:
            return ""