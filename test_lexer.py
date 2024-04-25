import unittest

from lexer import * 

class TestLexer(unittest.TestCase):
    def test_assign_statement(self):
        test_string = "x1 := x1 + 0"
        lex = Lexer(test_string)
        expected = [
            Token(VAR, "x1"),
            Token(ASSIGN, ":="),
            Token(VAR, "x1"),
            Token(ADD, "+"),
            Token(NUMBER, "0")
        ]
        result = []
        while x := lex.get_next_token(): 
            result.append(x)
        self.assertEqual(result,expected)

    def test_loop_statement(self):
        test_string = \
        """LOOP x1 DO
            x1 := x1 + 0
        END"""
        lex = Lexer(test_string)
        expected = [
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
        result = []
        while x := lex.get_next_token(): 
            result.append(x)
        self.assertEqual(result,expected)


    def test_while_statements(self):
        test_string = \
        """WHILE x1 != 0 DO
            x1 := x1 + 0
        END"""
        lex = Lexer(test_string)
        expected = [
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
        result = []
        while x := lex.get_next_token(): 
            result.append(x)
        self.assertEqual(result,expected)


if __name__ == "__main__":
    unittest.main()
