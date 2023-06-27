#!/usr/bin/env python

# ----------------------------------
# other.py
#
# Analizador Semántico
# ----------------------------------

import ply.yacc as yacc
from lexic import tokens, lexer

# Regla padre


def p_init(p):
    "init : cmmd"


def p_bool(p):
    """bool : TRUE
    | FALSE
    """


def p_num(p):
    """num : INT
    | FLOAT
    | RAT
    | COMPX
    """


def p_optr(p):
    """optr : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MODULE
    | EXPON
    """


def p_optn(p):
    "optn : num optr num"


def p_comptn(p):
    "comptn : obj comptr obj"


def p_comptr(p):
    """comptr : EQCOMP
    | LESSTH
    | LESSEQTH
    | GREATH
    | GREATEQTH
    | NOTEQ
    """


def p_var(p):
    """var : ID EQUALS obj
    | ID EQUALS ID
    | ID EQUALS NIL
    """


def p_func(p):
    """
    func : DEF ID LPAREN objs RPAREN cmmd END
    | DEF ID LPAREN RPAREN cmmd END
    | DEF ID cmmd END
    | DEF ID LPAREN objs RPAREN cmmd RETURN obj END
    | DEF ID LPAREN RPAREN cmmd RETURN obj END
    | DEF ID cmmd RETURN obj END
    """


def p_else(p):
    """else : ELSE comptn cmmd
    | ELSE bool cmmd
    """


def p_elsif(p):
    """elsif : ELSIF comptn cmmd
    | ELSIF bool cmmd
    """


def p_elses(p):
    """elses : else
    | elsif elses
    """


def p_contol_if(p):
    """control : IF comptn cmmd END
    | IF bool cmmd END
    | IF comptn cmmd elses END
    | IF bool cmmd elses END
    """


def p_control_unless(p):
    """control : UNLESS comptn COLON cmmd END
    | UNLESS bool COLON cmmd END
    | UNLESS comptn cmmd elses END
    | UNLESS bool cmmd elses END
    """


def p_when(p):
    """when : WHEN objs
    | WHEN objs THEN
    | WHEN comptn
    """


def p_whens(p):
    """whens : when
    | when whens
    """


def p_control_case(p):
    """control : CASE ID whens else END
    | CASE ID whens END
    """


def p_ids(p):
    """ids : ID
    | ID COMMA ids"""


def p_array(p):
    """array : LBRAKET objs RBRAKET
    | LBRAKET ids RBRAKET
    | LBRAKET objs COMMA ids RBRAKET
    | LBRAKET ids COMMA objs RBRAKET
    """


def p_struc_set(p):
    """struc : SET DOT NEW
    | SET DOT NEW LPAREN RPAREN
    | SET DOT NEW LPAREN array RPAREN
    | SET array
    """


def p_objs(p):
    """objs : obj
    | obj COMMA objs
    """


def p_obj(p):
    """obj : STRING
    | num
    | bool
    | range
    | matrix
    """


def p_range(p):
    """range : LPAREN INT DOT DOT INT RPAREN
    | INT DOT DOT INT
    | LPAREN STRING DOT DOT STRING
    | STRING DOT DOT STRING
    """


def p_cmmd(p):
    """cmmd : var
    | func
    | control
    | optn
    """

def p_matrix(p):
    "matrix : LBRAKET rows RBRAKET "

def p_rows(p):
    """rows : row
    | row COMMA rows"""

def p_row(p):
    "row : array"

def p_error(p):
    if p:
        print(f"Sintaxis inválida: {p.type}")
    else:
        print("Invalid syntax at EOF")


def main():
    parser = yacc.yacc(debug=1)

    while True:
        try:
            command = input("$ ")
        except EOFError:
            break
        if not command:
            continue
        result = parser.parse(command)
        if result != None:
            print(result)


if __name__ == "__main__":
    main()
