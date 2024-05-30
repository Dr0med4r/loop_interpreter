from tokens import *


class LexerError(Exception):
    pass

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
        if self.read_position >= self.input_length:
            return "\0"
        return self.input[self.read_position]

    def isspace(self, char: str) -> bool:
        return char in " \t\v"

    def skip_whitespace(self):
        while self.isspace(self.ch):
            self.read_char()

    def parse_input(self) -> list[Token]:
        self.position = 0
        self.read_position = 0
        self.ch = ""
        tokens = []
        while token := self.get_next_token():
            tokens.append(token)
        return tokens

    def get_next_token(self) -> Token | None:
        self.skip_whitespace()
        linenumber = self.input.count("\n", 0, self.position)
        if self.ch in ONECHAR_KEYWORDS:
            token = ONECHAR_KEYWORDS[self.ch]
            self.read_char()
            token.line_num = linenumber
            return token
        # NOTZERO
        elif self.ch == "!":
            while self.ch != "0":
                self.read_char()
            self.read_char()
            return Token("NOTZERO", "!= 0", linenumber)
        # ASSING
        elif self.ch == ":":
            if self.peek_char() == "=":
                self.read_char()
                self.read_char()
                return Token("ASSIGN", ":=", linenumber)
            else:
                raise LexerError(f"expected '=' not {self.ch} on line {linenumber}")
        # NUMBER
        elif self.ch.isdigit():
            pos = self.position
            while self.ch.isdigit():
                self.read_char()
            return Token("NUMBER", self.input[pos : self.position], linenumber)
        # EOF
        elif self.ch == "\0":
            return None
        # KEYWORDS
        else:
            pos = self.position
            while self.ch.isalnum():
                self.read_char()
            token_string = self.input[pos : self.position]
            # Character that is not correct is in string
            if len(token_string) <= 0:
                raise LexerError(f"expected no {self.ch} on line {linenumber}")
            if token_string in RESERVED_KEYWORDS:
                token = RESERVED_KEYWORDS[token_string]
                token.line_num = linenumber
                return token
            return Token(VAR, token_string, linenumber)
