from dataclasses import dataclass, field

from tree import Assignment, BinaryExpression, If, Loop, Program, Variable, While


class ExecuteError(Exception):
    pass


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

    def evaluate_binary_expression(self, left, operator, right) -> int:
        if type(left) == Variable:
            left_value = self.get(left)
        elif type(left) == int:
            left_value = left
        else:
            raise ExecuteError("expected Value")

        if type(right) == Variable:
            right_value = self.get(right)
        elif type(right) == int:
            right_value = right
        else:
            raise ExecuteError("expected Value")

        if operator == "+":
            value = left_value + right_value
        else:
            value = left_value - right_value
            if value < 0:
                value = 0
        return value

    def execute_assignment(
        self, left: Variable, right: BinaryExpression | Variable | int
    ):
        match right:
            case BinaryExpression(left=first, operator=operator, right=second):
                value = self.evaluate_binary_expression(first, operator, second)
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
