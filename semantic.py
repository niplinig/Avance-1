#!/usr/bin/env python

# ==============================================
#
# semantic.py
#
# Syntactic and Semantic Analysis
#
# ==============================================

import ply.yacc as yacc
from lexical import MyLexer
import io
import sys

# ----------------------------------
#
# 	Grammar Rule Functions
#
# ----------------------------------

start = 'init'

def p_init(p):
    "init : statements"
    line = p.lineno(0)
    index = p.lexpos(0)


def p_statement(p):
    """statement : assignment
    | function
    | control
    | arithmetic
    """
    line = p.lineno(0)
    index = p.lexpos(0)


def p_statements(p):
    """statements : statement
    | statement statements
    """
    line = p.lineno(0)
    index = p.lexpos(0)


def p_ids(p):
    """ids : ID
    | ID COMMA ids
    """
    line = p.lineno(0)
    index = p.lexpos(0)


def p_literal(p):
    """literal : STRING
    | boolean
    | numeric
    | range
    """
    line = p.lineno(0)
    index = p.lexpos(0)


def p_literals(p):
    """literals : literal
    | literal COMMA literals
    """
    line = p.lineno(0)
    index = p.lexpos(0)  


def p_boolean(p):
    """boolean : TRUE
    | FALSE
    """
    line = p.lineno(0)
    index = p.lexpos(0)


def p_numeric(p):
    """numeric : COMPLEX
    | RATIONAL
    | FLOAT
    | INTEGER
    """
    line = p.lineno(0)
    index = p.lexpos(0)


def p_arithmetic(p):
    """arithmetic : numeric PLUS numeric
    | numeric PLUS arithmetic
    | numeric MINUS numeric
    | numeric MINUS arithmetic
    | numeric EXPO numeric
    | numeric EXPO arithmetic
    | numeric MULT numeric
    | numeric MULT arithmetic
    | numeric DIV numeric
    | numeric DIV arithmetic
    | numeric MODULO numeric
    | numeric MODULO arithmetic
    """


def p_comparation(p):
    """comparation : literal EQUAL literal
    | ID EQUAL ID
    | literal NOT_EQ literal
    | ID NOT_EQ ID
    | literal LT_OR_EQ literal
    | ID LT_OR_EQ ID
    | literal GT_OR_EQ literal
    | ID GT_OR_EQ ID
    | literal LESS_THAN literal
    | ID LESS_THAN ID
    | literal GREATER_THAN literal
    | ID GREATER_THAN ID
    """


def p_comparations(p):
    """comparations : comparation AND comparation
    | comparation LOGIC_AND comparation
    | comparation AND comparations
    | comparation LOGIC_AND comparations
    | comparation OR comparation
    | comparation LOGIC_OR comparation
    | comparation OR comparations
    | comparation LOGIC_OR comparations
    | boolean AND boolean
    | boolean LOGIC_AND boolean
    | boolean OR boolean
    | boolean LOGIC_OR boolean
    """


def p_assignment(p):
    """assignment : ID ASSIGN ID
    | ID ASSIGN NIL
    | ID ASSIGN struc
    | ID ASSIGN literal
    | ID ASSIGN arithmetic
    """
    p[0] = p[2]

def p_assignment_operations(p):
    """assignment : ID ADD_ASSIGN ID
    | ID ADD_ASSIGN numeric
    | ID SUBS_ASSIGN ID
    | ID SUBS_ASSIGN numeric
    | ID MULT_ASSIGN ID
    | ID MULT_ASSIGN numeric
    | ID DIV_ASSIGN ID
    | ID DIV_ASSIGN numeric
    | ID MOD_ASSIGN ID
    | ID MOD_ASSIGN numeric
    """


def p_func(p):
    """function : DEF ID L_PAREN literals R_PAREN statements END
    | DEF ID L_PAREN R_PAREN statements END
    | DEF ID statements END
    | DEF ID L_PAREN literals R_PAREN statements RETURN ID END
    | DEF ID L_PAREN R_PAREN statements RETURN ID END
    | DEF ID statements RETURN ID END
    | DEF ID L_PAREN literals R_PAREN statements RETURN literal END
    | DEF ID L_PAREN R_PAREN statements RETURN literal END
    | DEF ID statements RETURN literal END
    """


def p_else(p):
    """else : ELSE boolean statements
    | ELSE comparation statements
    | ELSE comparations statements
    """


def p_elsif(p):
    """elsif : ELSIF boolean statements
    | ELSIF comparation statements
    | ELSIF comparations statements
    """


def p_elses(p):
    """elses : else
    | elsif elses
    """


def p_contol_if(p):
    """control : IF boolean statements END
    | IF comparation statements END
    | IF comparations statements END
    | IF boolean statements elses END
    | IF comparation statements elses END
    | IF comparations statements elses END
    """


def p_control_unless(p):
    """control : UNLESS boolean COLON statements END
    | UNLESS comparation COLON statements END
    | UNLESS comparations COLON statements END
    | UNLESS boolean statements elses END
    | UNLESS comparation statements elses END
    | UNLESS comparations statements elses END
    """


def p_when(p):
    """when : WHEN literal
    | WHEN literal THEN
    | WHEN comparation
    | WHEN comparations
    """


def p_whens(p):
    """whens : when
    | when whens
    """


def p_control_case(p):
    """control : CASE ID whens else END
    | CASE ID whens END
    """


def p_control_while(p):
    """control : WHILE boolean DO statements END
    | WHILE comparation DO statements END
    | WHILE comparations DO statements END
    """


def p_element(p):
    """element : ID
    | STRING
    | boolean
    | numeric
    | range
    """


def p_elements(p):
    """elements : element
    | element COMMA elements
    """


def p_array(p):
    """array : L_BRACKET literals R_BRACKET
    | L_BRACKET ids R_BRACKET
    | L_BRACKET elements R_BRACKET
    """


def p_arrays(p):
    """arrays : array
    | array COMMA arrays
    """


def p_struc(p):
    """struc : strucMatrix
    | strucSet
    | strucHash
    """    


def p_strucMatrix(p):
    "strucMatrix : MATRIX L_BRACKET arrays R_BRACKET"


def p_strucSet(p):
    """strucSet : SET PERIOD NEW
    | SET PERIOD NEW L_PAREN R_PAREN
    | SET PERIOD NEW L_PAREN array R_PAREN
    | SET array
    """


def p_strucHash(p):
    """strucHash : HASH PERIOD NEW
    | HASH PERIOD NEW L_BRACE R_BRACE
    | HASH PERIOD NEW L_BRACE hashelems R_BRACE
    | HASH array
    """


def p_hashelem_rocket(p):
    """hashelem : COLON ID RW_DOUBLE_ARROW literal
    | ID COLON literal
    | STRING COLON literal
    """


def p_hashelems(p):
    """hashelems : hashelem COMMA hashelem
    | hashelem COMMA hashelems
    """


def p_range(p):
    """range : L_PAREN INTEGER ELLIPSIS INTEGER R_PAREN
    | L_PAREN INTEGER DOUBLE_PERIOD INTEGER R_PAREN
    | INTEGER ELLIPSIS INTEGER
    | INTEGER DOUBLE_PERIOD INTEGER
    | L_PAREN STRING ELLIPSIS STRING
    | L_PAREN STRING DOUBLE_PERIOD STRING
    | STRING ELLIPSIS STRING
    | STRING DOUBLE_PERIOD STRING
    """


def p_error(p):
    if p:
        print(f"Invalid Syntax : {p.type}")
    else:
        print("Invalid Syntax EOF")


def get_title():
    return f"""
Syntactic Analysis
{('-') * 46}
"""


def yacc_data(data):
    parser = yacc.yacc()
    printing_data = get_title()

    # Redirigir la salida estándar a un objeto StringIO
    temp_out = io.StringIO()
    sys.stdout = temp_out

    # Realizar el análisis Sintáctico
    parser.parse(data)

    # Restaurar la salida estándar
    sys.stdout = sys.__stdout__

    # Obtener el valor impreso
    result_line = temp_out.getvalue()
    if result_line is not None:
        printing_data += result_line
    return printing_data


def yacc_shell():
    parser = yacc.yacc()
    print(get_title())
    while True:
        try:
            statement = input("$ ")
        except EOFError:
            break
        if not statement:
            continue
        if statement == "exit()":
            break
        result_line = parser.parse(statement)
        if result_line is not None:
            print(result_line)


def yacc_file(file_path):
    parser = yacc.yacc()
    printing_data = get_title()
    with open(file_path, mode="r", encoding="utf8") as data:
        data_lines = data.readlines()
        for line in data_lines:
            temp_out = io.StringIO()
            sys.stdout = temp_out
            parser.parse(line, tracking=True)
            sys.stdout = sys.__stdout__
            result_line = temp_out.getvalue()
            if result_line is not None:
                printing_data += result_line
    return printing_data
