#!/usr/bin/env python

# ----------------------------------
# other.py
#
# Analizador Semántico
# ----------------------------------

import ply.yacc as yacc
from main import lexer, tokens


def p_numeric_int(p):
    "numeric : INT"


def p_numeric_float(p):
    "numeric : FLOAT"


def p_addition(p):
    "addition : numeric PLUS numeric"


def p_substrac(p):
    "substrac : numeric MINUS numeric"


def main():
    parser = yacc.yacc(debug=1)

    while True:
        try:
            command = input(" >  ")
        except EOFError:
            break
        if not command:
            continue
        result = parser.parse(command)
        print(result)


if __name__ == "__main__":
    main()
