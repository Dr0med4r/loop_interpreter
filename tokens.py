
from dataclasses import dataclass


TokenType = str
@dataclass
class Token:
    type: TokenType
    content: str
    def __repr__(self) -> str:
        return f"<TokenType: {self.type}, content: {self.content}>"

# Std
LOOP = "LOOP"
DO = "DO"
END = "END"
VAR = "VAR"
ASSIGN = "ASSIGN"
ADD = "+"
SUB = "-"
DELIMITER = ";"
NUMBER = "NUMBER"
EOF = "EOF"

# Extension
IF = "IF"
THEN = "THEN"
NOTZERO = "!= 0"
WHILE = "WHILE"


ONECHAR_KEYWORDS = {
    "+": Token("ADD", ADD),
    "-": Token("SUB", SUB),
    ";": Token("DELIMITER", DELIMITER),
    "\n": Token("DELIMITER", DELIMITER)
}

RESERVED_KEYWORDS = {
    "LOOP": Token(LOOP, LOOP),
    "DO": Token(DO, DO),
    "END": Token(END, END),
    "VAR": Token(VAR, VAR),
    "IF": Token(IF, IF),
    "THEN": Token(THEN, THEN),
    "WHILE": Token(WHILE, WHILE)
}
