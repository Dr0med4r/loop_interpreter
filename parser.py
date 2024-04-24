from tree import Program

from tokens import DELIMITER, Token
DELIMITER = Token("DELIMITER", DELIMITER)

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.position = 0
        self.read_position = 0
        self.current = tokens[0]
        self.tokens_length = len(tokens)
        self.program = Program([])

    def progress(self):
        if(self.position >= self.tokens_length):
            return
        self.position = self.read_position
        self.current = self.peek()
        self.read_position += 1

    def peek(self) -> Token|None:
        if(self.read_position >= self.tokens_length):
            return None
        return self.tokens[self.read_position]

    def parse_statements(self) -> list[Token]:
        pos = self.position
        while self.current != DELIMITER:
            self.progress()
        end_pos = self.position
        self.progress()
        return self.tokens[pos:end_pos]
    
