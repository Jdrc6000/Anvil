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
    children: TypingList[Node]

@dataclass
class Paragraph(Node):
    children: TypingList[Node]

@dataclass
class Bold(Node):
    children: TypingList[Node]

@dataclass
class Italic(Node):
    children: TypingList[Node]

@dataclass
class ListItem(Node):
    children: TypingList[Node]

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
    children: TypingList[Node]

@dataclass
class Text(Node):
    value: str