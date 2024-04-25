import logging

from tokens import *

logger = logging.getLogger(__name__)

class Lexer:
    def __init__(self, input) -> None:
        self.input = input
        self.input_length = len(input)
        self.position = 0
        self.read_position = 0
        self.ch = ""

    def read_char(self) -> None:
        self.position = self.read_position
        self.ch = self.peek_char()
        self.read_position += 1

    def peek_char(self) -> str:
        if(self.read_position >= self.input_length):
            return "\0"
        return self.input[self.read_position]

    def isspace(self,char: str) -> bool:
        return char in " \t\v"

    def skip_whitespace(self):
        while self.isspace(self.ch):
            self.read_char()


    def get_next_token(self) -> Token|None:
        self.skip_whitespace()
        if self.ch in ONECHAR_KEYWORDS:
            token = ONECHAR_KEYWORDS[self.ch]
            self.read_char()
            return token
        elif self.ch == "!":
            while self.ch != "0":
                self.read_char()
            self.read_char()
            return Token("NOTZERO", "!= 0")
        elif self.ch == ":":
            if self.peek_char() == "=":
                self.read_char()
                self.read_char()
                return Token("ASSIGN", ":=")
            else: 
                logger.error(f"expected = not {self.ch} on position {self.position}")
                exit()
        elif self.ch.isdigit():
            pos = self.position
            while self.ch.isdigit():
                self.read_char()
            return Token("NUMBER",self.input[pos:self.position])
        elif self.ch == "\0":
            return None
        else:
            pos = self.position 
            while self.ch.isalnum():
                self.read_char()
            token = self.input[pos:self.position]
            if token in RESERVED_KEYWORDS:
                return RESERVED_KEYWORDS[token]
            return Token(VAR, token)
