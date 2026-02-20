from dataclasses import dataclass
from typing import Any, Optional
from src.lexer.token_types import TokenType

@dataclass
class Token:
    type: TokenType
    level: Optional[int] = None
    content: Optional[Any] = None

    def __repr__(self):
        if self.level is not None and self.content is not None:
            return f"{self.type.name}:{self.level}:{self.content}"
        elif self.content is not None:
            return f"{self.type.name}:{self.content}"
        return f"{self.type.name}"