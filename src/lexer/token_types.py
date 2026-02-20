from enum import Enum, auto

class TokenType(Enum):
    HEADER = auto()
    BOLT = auto()
    ITALIC = auto()
    LINK = auto()
    IMAGE = auto()
    CODE_BLOCK = auto()
    INLINE_CODE = auto()
    LIST_ITEM = auto()
    PARAGRAPH = auto()