from abc import ABC
from dataclasses import dataclass


@dataclass
class Statement:
    pass


@dataclass
class Program(object):
    statements: list

    def add_statement(self, statement):
        self.statements.append(statement)


@dataclass
class Variable(Statement):
    name: str


@dataclass
class BinaryExpression(Statement):
    left: Variable
    operator: str
    right: Variable | int


@dataclass
class Assignment(Statement):
    left: Variable
    right: BinaryExpression | Variable | int


@dataclass
class BlockStatement(ABC, Statement):
    var: Variable
    program: Program


@dataclass
class Loop(BlockStatement):
    pass


@dataclass
class While(BlockStatement):
    pass


@dataclass
class If(BlockStatement):
    pass
