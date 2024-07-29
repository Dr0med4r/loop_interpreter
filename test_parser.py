import unittest

from parser import *
from tokens import IF, NOTZERO
from tree import If


class TestParser(unittest.TestCase):

    def test_assign_variable_number(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0"),
        ]

        expected = Program(
            [Assignment(Variable("x1"), BinaryExpression(Variable("x1"), "+", 0))]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_assign_number_variable(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(NUMBER, "0"),
            Token(ADD, "+"),
            Token(VAR, "x1"),
        ]

        expected = Program(
            [Assignment(Variable("x1"), BinaryExpression(0, "+", Variable("x1")))]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_assign_variable(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x2"),
        ]

        expected = Program([Assignment(Variable("x1"), Variable("x2"))])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_assign_number(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(NUMBER, "0"),
        ]

        expected = Program([Assignment(Variable("x1"), 0)])
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_assign_variable_variable(self):
        program = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(VAR, "x2"),
        ]

        expected = Program(
            [
                Assignment(
                    Variable("x1"),
                    BinaryExpression(Variable("x1"), "+", Variable("x2")),
                )
            ]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_loop(
        self,
    ):
        program = [
            Token(LOOP, LOOP),
            Token(VAR, "x1"),
            Token(DO, DO),
            Token(DELIMITER, ";"),
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0"),
            Token(DELIMITER, ";"),
            Token(END, END),
        ]
        expected = Program(
            [
                Loop(
                    Variable("x1"),
                    Program(
                        [
                            Assignment(
                                Variable("x1"), BinaryExpression(Variable("x1"), "+", 0)
                            )
                        ]
                    ),
                )
            ]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_nested_loop(
        self,
    ):
        program = [
            Token(LOOP, LOOP),
            Token(VAR, "x1"),
            Token(DO, DO),
            Token(DELIMITER, ";"),
            Token(LOOP, LOOP),
            Token(VAR, "x1"),
            Token(DO, DO),
            Token(DELIMITER, ";"),
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0"),
            Token(DELIMITER, ";"),
            Token(END, END),
            Token(END, END),
        ]
        expected = Program(
            [
                Loop(
                    Variable("x1"),
                    Program(
                        [
                            Loop(
                                Variable("x1"),
                                Program(
                                    [
                                        Assignment(
                                            Variable("x1"),
                                            BinaryExpression(Variable("x1"), "+", 0),
                                        )
                                    ]
                                ),
                            )
                        ]
                    ),
                )
            ]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_while(
        self,
    ):
        program = [
            Token(WHILE, WHILE),
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
            Token(END, END),
        ]
        expected = Program(
            [
                While(
                    Variable("x1"),
                    Program(
                        [
                            Assignment(
                                Variable("x1"), BinaryExpression(Variable("x1"), "+", 0)
                            )
                        ]
                    ),
                )
            ]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)

    def test_if(
        self,
    ):
        program = [
            Token(IF, IF),
            Token(VAR, "x1"),
            Token(NOTZERO, "!= 0"),
            Token(THEN, THEN),
            Token(DELIMITER, ";"),
            Token(VAR, "x"),
            Token(ASSIGN, ":="),
            Token(VAR, "x"),
            Token(DELIMITER, ";"),
            Token(END, END),
        ]
        expected = Program(
            [If(Variable("x1"), Program([Assignment(Variable("x"), Variable("x"))]))]
        )
        parse = Parser(program)
        result = parse.parse_program()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
