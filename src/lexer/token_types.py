from enum import Enum, auto

class TokenType(Enum):
    HEADER = auto()
    BOLD = auto()
    ITALIC = auto()
    LINK = auto()
    IMAGE = auto()
    CODE_BLOCK = auto()
    INLINE_CODE = auto()
    LIST_ITEM = auto()
    ORDERED_LIST_ITEM = auto()
    BLOCKQUOTE = auto()
    PARAGRAPH = auto()
    TEXT = auto()
    BLANK_LINE = auto()
    EOF = auto()
    HR = auto()