from dataclasses import dataclass
from typing import List as TypingList, Optional, Any

@dataclass
class Node:
    pass

@dataclass
class Document:
    children: TypingList[Node]

@dataclass
class Heading(Node):
    level: int
    content: str

@dataclass
class Paragraph(Node):
    content: str

@dataclass
class Bold(Node):
    content: str

@dataclass
class Italic(Node):
    content: str

@dataclass
class ListItem(Node):
    content: str

@dataclass
class List(Node):
    items: TypingList[ListItem]

@dataclass
class Link(Node):
    text: str
    url: str

@dataclass
class Image(Node):
    alt: str
    src: str

@dataclass
class CodeBlock(Node):
    language: str
    content: str