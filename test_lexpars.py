import unittest

from lexer import Lexer
from parser import Parser


class TestLexParse(unittest.TestCase):
    def test_integration(
        self,
    ):
        test_string = """
        x3 := x1-x2
        x0 := x2
        LOOP x3 DO
            x0 := 0
            x0 := x0 + x1
        END
        """
        lex = Lexer(test_string)
        tokens = lex.parse_input()
        parse = Parser(tokens)
        print(parse.parse_program())


"""
Program(statements=[
    Assignment(
        left=Variable(name='x3'), 
        right=BinaryExpression(left=Variable(name='x1'), operator='-', right=Variable(name='x2'))
    ),
    Assignment(
        left=Variable(name='x0'), 
        right=Variable(name='x2')
    ),
    Loop(
        var=Variable(name='x3'),
        program=Program(statements=[
            Assignment(
                left=Variable(name='x0'),
                right=0
            ), 
            Assignment(
                left=Variable(name='x0'), 
                right=BinaryExpression(left=Variable(name='x0'), operator='+', right=Variable(name='x1'))
            )
        ])
    )
])
"""

if __name__ == "__main__":
    unittest.main()
