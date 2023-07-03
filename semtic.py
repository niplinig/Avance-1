#!/usr/bin/env python

# ----------------------------------
# other.py
#
# Analizador Semántico
# ----------------------------------

import ply.yacc as yacc
from lexic import tokens, lexer
from yachalk import chalk

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


def p_comptr(p):
    """comptr : EQCOMP
    | LESSTH
    | LESSEQTH
    | GREATH
    | GREATEQTH
    | NOTEQ
    """


def p_comptn(p):
    "comptn : obj comptr obj"


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


def p_strucSet(p):
    """strucSet : SET DOT NEW
    | SET DOT NEW LPAREN RPAREN
    | SET DOT NEW LPAREN array RPAREN
    | SET array
    """


def p_strucHash(p):
    """strucHash : HASH DOT NEW
    | HASH DOT NEW LBRACE RBRACE
    | HASH DOT NEW LBRACE hashelems RBRACE
    | HASH array
    """


def p_hashelem_rocket(p):
    "hashelem : COLON ID ROCKET obj"


def p_hashelem_json(p):
    "hashelem : ID COLON obj"


def p_hashelem_string(p):
    "hashelem : STRING COLON obj"


def p_hashelems(p):
    """hashelems : hashelem COMMA hashelem
    | hashelem COMMA hashelems
    """


def p_control_while(p):
    """control : WHILE comptn DO cmmd END
    | WHILE bool DO cmmd END
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
    | strucSet
    | strucHash
    | strucMatrix
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


def p_strucMatrix(p):
    "strucMatrix : MATRIX LBRAKET arrays RBRAKET"


def p_arrays(p):
    """arrays : array
    | array COMMA arrays"""


def p_error(p):
    if p:
        print(f"{chalk.bold.black('Invalid Syntax :')} {p.type}")
    else:
        print(f"Invalid Syntax EOF")


def yacc_shell():
    parser = yacc.yacc()

    while True:
        try:
            command = input("$ ")
        except EOFError:
            break
        if not command:
            continue
        if command == "exit()":
            break
        result = parser.parse(command, tracking=True)
        if result is not None:
            print(result)


def yacc_file(file_path):
    parser = yacc.yacc()

    with open(file_path, mode="r", encoding="utf8") as data:
        data_lines = data.readlines()
        for i, line in enumerate(data_lines):
            result = parser.parse(line, tracking=True)
            if result is not None:
                print(result)
