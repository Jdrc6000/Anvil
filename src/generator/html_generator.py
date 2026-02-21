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
            return f"<h{node.level}>{inner}</h{node.level}>\n"
        
        elif isinstance(node, Paragraph):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<p>{inner}</p>\n"
        
        elif isinstance(node, Bold):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<strong>{inner}</strong>"
        
        elif isinstance(node, Italic):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<em>{inner}</em>"
        
        elif isinstance(node, InlineCode):
            return f"<code>{node.value}</code>"
        
        elif isinstance(node, List):
            items_html = "".join(self.generate(item) for item in node.items)
            return f"<ul>\n{items_html}</ul>\n"
        
        elif isinstance(node, ListItem):
            inner = "".join(self.generate(c) for c in node.children)
            return f"  <li>{inner}</li>\n"
        
        elif isinstance(node, OrderedList):
            items_html = "".join(self.generate(item) for item in node.items)
            return f"<ol>\n{items_html}</ol>\n"
        
        elif isinstance(node, OrderedListItem):
            inner = "".join(self.generate(c) for c in node.children)
            return f"  <li>{inner}</li>\n"
        
        elif isinstance(node, Blockquote):
            inner = "".join(self.generate(c) for c in node.children)
            return f"<blockquote>{inner}</blockquote>\n"
        
        elif isinstance(node, CodeBlock):
            lang_attr = f' class="language-{node.language}"' if node.language else ""
            return f"<pre><code{lang_attr}>{node.code}</code></pre>\n"
            
        elif isinstance(node, Link):
            return f'<a href="{node.url}">{node.text}</a>'
        
        elif isinstance(node, Image):
            return f'<img src="{node.src}" alt="{node.alt}">'
        
        elif isinstance(node, HorizontalRule):
            return "<hr>\n"
        
        elif isinstance(node, Text):
            return node.value
        
        else:
            return ""