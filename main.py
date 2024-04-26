from exec import Execute
from lexer import Lexer
from parser import Parser
from tree import Variable

input = \
"""
x1 := 5
WHILE x1 != 0 DO 
    x0:=x0+5
    IF x1 != 0 THEN
    x1 := x1 - 1
    END
END
"""

if __name__ == "__main__":
    lex = Lexer(input)
    tokens = lex.parse_input()
    pars = Parser(tokens)
    program = pars.parse_program()
    exec = Execute()
    exec.set(Variable("x1"), 5)
    exec.execute_program(program)
    output = exec.get(Variable("x0"))

    print(f"Input:\n {input}\n\n")
    print(f"Output: {output}")
