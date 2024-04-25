import unittest

from parser import *
from tokens import NOTZERO

class TestParser(unittest.TestCase):

    def test_assign_variable_number(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0")
        ]

        expected = Program([
            Assignment(Variable("x1"),BinaryExpression(Variable("x1"),"+",0))
        ])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_assign_variable(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x2"),
        ]

        expected = Program([
            Assignment(Variable("x1"),Variable("x2"))
        ])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)


    def test_assign_number(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(NUMBER, "0"),
        ]

        expected = Program([
            Assignment(Variable("x1"),0)
        ])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_assign_variable_variable(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(VAR, "x2")
        ]

        expected = Program([
            Assignment(Variable("x1"),BinaryExpression(Variable("x1"),"+",Variable("x2")))
        ])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_loop(self, ):
        program = [
            Token(LOOP,LOOP),
            Token(VAR, "x1"),
            Token(DO, DO),
            Token(DELIMITER, ";"),

            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0"),
            Token(DELIMITER, ";"),

            Token(END,END)
        ]
        expected = Program([
            Loop(
                Variable("x1"),
                Program([
                     Assignment(Variable("x1"),BinaryExpression(Variable("x1"),"+",0))
                ])
            )
        ])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_while(self, ):
        program = [
            Token(WHILE,WHILE),
            Token(VAR, "x1"),
            Token(NOTZERO, "!= 0"),
            Token(DO, DO),
            Token(DELIMITER, ";"),

            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0"),
            Token(DELIMITER, ";"),

            Token(END,END)
        ]
        expected = Program([
            While(
                Variable("x1"),
                Program([
                     Assignment(Variable("x1"),BinaryExpression(Variable("x1"),"+",0))
                ])
            )
        ])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
