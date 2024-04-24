
from tokens import DELIMITER, Token
DELIMITER = Token("DELIMITER", DELIMITER)

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.position = 0
        self.current = tokens[0]
        self.tokens_length = len(tokens)

    def progress(self):
        if(self.position >= self.tokens_length):
            return
        self.position += 1
        self.current = self.tokens[self.position]

    def parse_statements(self):
        while self.current != DELIMITER:
            self.progress()

