from dataclasses import dataclass, field


TokenType = str


@dataclass
class Token:
    type: TokenType
    content: str
    line_num: int = field(default=-1, compare=False)


# Std
LOOP = "LOOP"
DO = "DO"
END = "END"
VAR = "VAR"
ASSIGN = "ASSIGN"
ADD = "ADD"
SUB = "SUB"
DELIMITER = "DELIMITER"
NUMBER = "NUMBER"
EOF = "EOF"

# Extension
IF = "IF"
THEN = "THEN"
NOTZERO = "NOTZERO"
WHILE = "WHILE"


ONECHAR_KEYWORDS = {
    "+": Token(ADD, "+"),
    "-": Token(SUB, "-"),
    ";": Token(DELIMITER, ";"),
    "\n": Token(DELIMITER, ";"),
}

RESERVED_KEYWORDS = {
    "LOOP": Token(LOOP, LOOP),
    "DO": Token(DO, DO),
    "END": Token(END, END),
    "VAR": Token(VAR, VAR),
    "IF": Token(IF, IF),
    "THEN": Token(THEN, THEN),
    "WHILE": Token(WHILE, WHILE),
}
