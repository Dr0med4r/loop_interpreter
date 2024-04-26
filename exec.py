from dataclasses import dataclass, field
import logging

from tree import Assignment, BinaryExpression, If, Loop, Program, Variable, While

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="{levelname}:{module}:{funcName}:{lineno}: {message}",
    style="{",
)


@dataclass
class Execute:
    variables: dict[str, int] = field(default_factory=dict)

    def execute_program(self, program):
        for statement in program.statements:
            match statement:
                case Assignment(left=left, right=right):
                    self.execute_assignment(left, right)
                case Loop(var=var, program=program):
                    self.execute_loop(var, program)
                case While(var=var, program=program):
                    self.execute_while(var, program)
                case If(var=var, program=program):
                    self.execute_if(var, program)

    def get(self, variable: Variable) -> int:
        if variable.name in self.variables.keys():
            return self.variables[variable.name]
        else:
            self.variables[variable.name] = 0
            return 0

    def set(self, variable: Variable, value: int):
        if value < 0:
            value = 0
        self.variables[variable.name] = value

    def execute_assignment(
        self, left: Variable, right: BinaryExpression | Variable | int
    ):
        match right:
            case BinaryExpression(left=first, operator=operator, right=second):
                if operator == "+":
                    value = None
                    if type(second) is Variable:
                        value = self.get(first) + self.get(second)
                    elif type(second) is int:
                        value = self.get(first) + second
                    if value == None:
                        logger.error("expected Value")
                        exit()
                    self.set(left, value)
                else:
                    value = None
                    if type(second) is Variable:
                        value = self.get(first) - self.get(second)
                    elif type(second) is int:
                        value = self.get(first) - second
                    if value == None:
                        logger.error("expected Value")
                        exit()
                    if value < 0:
                        value = 0
                    self.set(left, value)
            case Variable():
                self.set(left, self.get(right))
            case integer:
                self.set(left, integer)

    def execute_loop(self, var: Variable, program: Program):
        for _ in range(self.get(var)):
            self.execute_program(program)

    def execute_while(self, var: Variable, program: Program):
        while self.get(var) != 0:
            self.execute_program(program)

    def execute_if(self, var: Variable, program: Program):
        if self.get(var) != 0:
            self.execute_program(program)
