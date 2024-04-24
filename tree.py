from dataclasses import dataclass

@dataclass
class Statement():
    pass

@dataclass
class Program(object):
    statements: list

@dataclass
class Variable(Statement):
    name: str

@dataclass
class BinaryExpression(Statement):
    left: Variable
    operator: str
    right: (Variable|int)

@dataclass
class Assignment(Statement):
    left: Statement
    right: (BinaryExpression|Variable|int)


@dataclass
class Loop(Statement):
    var: Variable
    program: Program

@dataclass
class While(Loop):
    pass



