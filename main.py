from lexer import Lexer
input = """x3 := x1 + 0
x4 := x3 + 1 
x4 := x4 - x2 
WHILE x4 != 0 DO 
    x0 := x0 + 1 
    x3 := x3 - x2
    x4 := x3 + 1
    x4 := x4 - x2
END 
"""

if __name__ == "__main__":
    lex = Lexer(input)
    while x := lex.get_next_token(): 
        print(x)
