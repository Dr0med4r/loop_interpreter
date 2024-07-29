import unittest


from parser import *
from exec import Execute


class TestLexParse(unittest.TestCase):
    def test_assign(
        self,
    ):

        exec = Execute()
        test_program = Program(
            [Assignment(Variable("x1"), BinaryExpression(1, "+", Variable("x1")))]
        )
        exec.set(Variable("x1"), 5)
        exec.execute_program(test_program)
        self.assertEqual(exec.get(Variable("x1")), 6)

        test_program = Program(
            [Assignment(Variable("x1"), BinaryExpression(Variable("x1"), "+", 1))]
        )
        exec.set(Variable("x1"), 5)
        exec.execute_program(test_program)
        self.assertEqual(exec.get(Variable("x1")), 6)

        test_program = Program(
            [
                Assignment(
                    Variable("x1"),
                    BinaryExpression(Variable("x1"), "+", Variable("x1")),
                )
            ]
        )
        exec.set(Variable("x1"), 5)
        exec.execute_program(test_program)
        self.assertEqual(exec.get(Variable("x1")), 10)


if __name__ == "__main__":
    unittest.main()
