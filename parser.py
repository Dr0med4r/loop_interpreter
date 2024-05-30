import logging

from tree import (
    Assignment,
    BinaryExpression,
    If,
    Loop,
    Program,
    Statement,
    Variable,
    While,
)
from tokens import (
    ADD,
    ASSIGN,
    DELIMITER,
    DO,
    END,
    EOF,
    LOOP,
    NOTZERO,
    NUMBER,
    SUB,
    THEN,
    VAR,
    WHILE,
    Token,
)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="{levelname}:{module}:{funcName}:{lineno}: {message}",
    style="{",
)

StopParse = str
END_EXPRESSION = "STOP"

class ParserException(Exception):
    pass

class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.position = 0
        self.read_position = 0
        self.current = tokens[0]
        self.tokens_length = len(tokens)
        self.program = Program([])
        self.next_token()

    def next_token(self):
        self.position = self.read_position
        self.current = self.peek()
        self.read_position += 1

    def peek(self) -> Token:
        if self.read_position >= self.tokens_length:
            return Token(EOF, EOF)
        return self.tokens[self.read_position]

    def skip_delimiters(self):
        while self.current.type == DELIMITER:
            self.next_token()

    def check_token(self, check_types: list[str]):
        if self.current.type == EOF and EOF not in check_types:
            raise ParserException(f"expected another Token")
        if self.current.type not in check_types:
            raise ParserException(f"expected {check_types} got {self.current.type} on line {self.current.line_num}")

    def parse_program(self) -> Program:
        program = Program([])
        while self.current != Token(EOF, EOF):
            statement = self.parse_statement()
            if statement != END_EXPRESSION:
                program.add_statement(statement)
        return program

    """
    returns statements and END_EXPRESSION if the Program is finished
    """

    def parse_statement(self) -> Statement | StopParse:
        self.skip_delimiters()
        match self.current:
            case Token(type="LOOP"):
                return self.parse_loop_statement()
            case Token(type="WHILE"):
                return self.parse_while_statement()
            case Token(type="VAR"):
                return self.parse_assign_statement()
            case Token(type="IF"):
                return self.parse_if()
            case Token(type="EOF"):
                return END_EXPRESSION
            case Token(type="END"):
                return END_EXPRESSION
            case _:
               raise ParserException(
                    f"found {self.current.type} but expected new statement on line {self.current.line_num}"
                )

    def parse_assign_statement(self) -> Assignment:
        self.check_token([VAR])
        var = Variable(self.current.content)
        self.next_token()
        self.check_token([ASSIGN])
        self.next_token()
        right = -1
        match self.current:
            case Token(type="VAR"):
                self.check_token([VAR])
                if self.peek().type in [ADD, SUB]:
                    lexpr = Variable(self.current.content)
                    self.next_token()
                    self.check_token([ADD, SUB])
                    operation = self.current.content
                    self.next_token()
                    rexpr = 0
                    if self.current.type == VAR:
                        rexpr = Variable(self.current.content)
                    else:
                        self.check_token([NUMBER])
                        rexpr = int(self.current.content)
                    right = BinaryExpression(lexpr, operation, rexpr)
                else:
                    right = Variable(self.current.content)
            case Token(type="NUMBER"):
                self.check_token([NUMBER])
                right = int(self.current.content)
            case _:
                self.check_token([])
        self.next_token()
        self.check_token([DELIMITER, EOF])
        if right == -1:
            raise ParserException(
                f"failed to parse right side expression on line {self.current.line_num}"
            )
        assignment = Assignment(var, right)
        return assignment

    def parse_loop_statement(self) -> Loop:
        self.next_token()
        self.check_token([VAR])
        var = Variable(self.current.content)
        self.next_token()
        self.skip_delimiters()
        self.check_token([DO])
        self.next_token()
        self.skip_delimiters()
        program = Program([])
        while self.current.type != END:
            statement = self.parse_statement()
            if statement != END_EXPRESSION:
                program.add_statement(statement)
        self.check_token([END])
        self.next_token()
        expression = Loop(var, program)
        return expression

    def parse_while_statement(self) -> While:
        self.next_token()
        self.check_token([VAR])
        var = Variable(self.current.content)
        self.next_token()
        self.check_token([NOTZERO])
        self.next_token()
        self.skip_delimiters()
        self.check_token([DO])
        self.next_token()
        self.skip_delimiters()
        program = Program([])
        while self.current.type != END:
            statement = self.parse_statement()
            if statement != END_EXPRESSION:
                program.add_statement(statement)
        self.check_token([END])
        self.next_token()
        statement = While(var, program)
        return statement

    def parse_if(self) -> If:
        self.next_token()
        self.check_token([VAR])
        var = Variable(self.current.content)
        self.next_token()
        self.check_token([NOTZERO])
        self.next_token()
        self.skip_delimiters()
        self.check_token([THEN])
        self.next_token()
        self.skip_delimiters()
        program = Program([])
        while self.current.type != END:
            statement = self.parse_statement()
            if statement != END_EXPRESSION:
                program.add_statement(statement)
        self.check_token([END])
        self.next_token()
        statement = If(var, program)
        return statement
