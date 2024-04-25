# LOOP 

## Ausdrücke
`x := y + n`
`x := y - n`
für alle $x,y \in V$ und $n \in \mathbb{N}$

Wenn $P_1$ und $P_2$ LOOP Programme sind dann auch $P_1;P_2$ ; kann auch durch \n ersetzt werden 

Wenn $P$ ein LOOP Programm dann auch 
`LOOP x DO 
    P 
END`

## Abarbeitung
`x := y + n` Variable x wird als neuer Wert die Summe des Wertes für y und der Zahl n zugewiesen 

`x := y - n` Variable x wird als neuer Wert die Differenz des Wertes für y und der Zahl n zugewiesen falls diese kleiner als 0 ist wird 0 zugewiesen 

`LOOP x DO 
    P 
END`: P wird genau n-mal ausgeführt wobei n der Anfangswert von x ist 

## Ausgabe 
Das Ergebnis ist der Wert der Variable x0 

## Makros

`x := y` 

    `x := y + 0`

`x := 0`

    `LOOP x DO
        x := x - 1
    END`

`x := n` (natürliche Zahl n)
    
    `x:= 0
    x := x + n`

`x := y + z`

    `x := y
    LOOP z DO
        x := x + 1
    END`

`IF x!=0 THEN
    P
END`

    `LOOP x DO y := 1 END
    LOOP y DO P END`

# WHILE 
Zusätzlich noch WHILE 

`WHILE x != 0 DO 
    P 
END`


## Grammar
Program ::= Statement*

Statement ::= (Assignment | Loop | While | If) Delimiter

Assignment ::= Var ":=" ((Var ("+"|"-") (Number|Var))| Var | Number )

Number ::= [0-9]

Var ::= [a-zA-Z][a-zA-Z0-9]*

Delimiter ::= (";"|"\n")

Loop ::= "LOOP" Var "DO" Program "END"

While ::= "WHILE" Var "!= 0" "DO" Program "END"

If ::= "IF" Var "!= 0" "DO" Program "END"
