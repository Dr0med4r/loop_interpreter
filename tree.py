from dataclasses import dataclass

@dataclass
class Statement():
    pass

@dataclass
class Program(object):
    statements: list

@dataclass
class Assignment(Statement):
    left: Statement
    right: Statement

@dataclass
class Variable(Statement):
    name: str

@dataclass
class Loop(Statement):
    var: Statement
    program: Statement

@dataclass
class While(Loop):
    pass


@dataclass
class BinaryExpression(Statement):
    left: Variable
    operator: str
    right: (Variable|int)


