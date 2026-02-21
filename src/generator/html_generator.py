from src.parser.ast_nodes import *

class Generator:
    def __init__(self, tree):
        self.tree = tree
    
    def generate(self, node):
        if isinstance(node, Document):
            return "".join([self.generate(child) for child in node.children])
        
        elif isinstance(node, Heading):
            return f"<h{node.level}>{node.content}</h{node.level}>"

        elif isinstance(node, Bold):
            return f"<strong>{node.content}</strong>"

        elif isinstance(node, Italic):
            return f"<em>{node.content}</em>"

        elif isinstance(node, Paragraph):
            return f"<p>{node.content}</p>"
        
        elif isinstance(node, str):
            return node

        else:
            return ""