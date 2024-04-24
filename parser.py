from tree import Assignment, BinaryExpression, Loop, Program, Variable

from tokens import ADD, ASSIGN, DELIMITER, EOF, LOOP, NUMBER, SUB, VAR, WHILE, Token
DELIMITER = Token("DELIMITER", DELIMITER)

class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.position = 0
        self.read_position = 0
        self.current = tokens[0]
        self.tokens_length = len(tokens)
        self.program = Program([])

    def next_token(self):
        if(self.position >= self.tokens_length):
            return
        self.position = self.read_position
        self.current = self.peek()
        self.read_position += 1

    def peek(self) -> Token:
        if(self.read_position >= self.tokens_length):
            return Token(EOF,EOF)
        return self.tokens[self.read_position]

    def check_token(self, type: list[str]):
        if(self.current is None):
            print(f"expected another Token")
            exit()
        if(self.current.type not in type):
            print(f"expected {type} got {self.current.type}")

    def parse_statement(self):
        match self.current:
            case Token.type if type == LOOP:
                return self.parse_loop_statement()
            # case Token.type if type == WHILE: 
            #     return self.parse_while_statement()
            case Token.type if type == VAR:
                return self.parse_assign_statement()

    def parse_assign_statement(self):
        self.check_token([VAR])
        assert self.current is not None
        var = Variable(self.current.content)
        self.next_token()
        self.check_token([ASSIGN])
        self.next_token()
        right = 0
        if(self.current.type == VAR): 
            if(self.peek().type == ADD or self.peek().type == SUB):
                lexpr = Variable(self.current.content)
                self.next_token()
                self.check_token([ADD,SUB])
                operation = self.current.content 
                self.next_token()
                rexpr = 0
                if(self.current.type == VAR):
                    rexpr = Variable(self.current.content)
                else:
                    rexpr = int(self.current.content)
                right = BinaryExpression(lexpr,operation,rexpr)
            else:
                right = Variable(self.current.content)
        else:
            self.check_token([NUMBER])
            right = int(self.current.content)
        self.next_token()
        assignment = Assignment(var,right)
        return assignment
    
    def parse_loop_statement(self):
        pos = self.position
        self.next_token()
        if self.current is None:
            print(f"expected VAR")
            exit()

        if (self.current.type != "VAR"):
            print(f"expected VAR but got {self.current.type}")
            exit()
        var = Variable(self.current.content)
        self.next_token() 
        if (self.current.type != "DO"):
            print(f"expected DO but got {self.current.type}")
            exit()
        self.next_token()
        program = self.parse_statement()

        exp = Loop(var,program)
