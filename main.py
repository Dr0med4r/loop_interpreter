#!/usr/bin/env python

import sys

from exec import Execute
from lexer import Lexer
from parser import Parser
from tree import Variable


def execute():
    filename = sys.argv[1]
    with open(filename) as file:
        input = file.read()
    lex = Lexer(input)
    tokens = lex.parse_input()
    pars = Parser(tokens)
    program = pars.parse_program()
    exec = Execute()
    for index, value in enumerate(sys.argv[2:]):
        exec.set(Variable(f"x{index + 1}"), int(value))
    exec.execute_program(program)
    output = exec.get(Variable("x0"))

    print(f"Input:\n {input}\n\n")
    print(f"Output: {output}")


if __name__ == "__main__":
    execute()
