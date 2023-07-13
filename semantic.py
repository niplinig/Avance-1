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
from contextlib import redirect_stdout
from io import StringIO

# ----------------------------------
#
# 	Grammar Rule Functions
#
# ----------------------------------


class MyYacc(object):
    tokens = MyLexer.tokens

    start = "init"

    def p_init(self, p):
        "init : statements"
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_statement(self, p):
        """statement : assignment
        | function
        | control
        | arithmetic
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_statements(self, p):
        """statements : statement
        | statement statements
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_ids(self, p):
        """ids : ID
        | ID COMMA ids
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_literal(self, p):
        """literal : STRING
        | ID
        | boolean
        | numeric
        | range
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_literals(self, p):
        """literals : literal
        | literal COMMA literals
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_boolean(self, p):
        """boolean : TRUE
        | FALSE
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_numeric(self, p):
        """numeric : COMPLEX
        | RATIONAL
        | FLOAT
        | INTEGER
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_value(self, p):
        """value : numeric
        | ID
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_arithmetic(self, p):
        """arithmetic : value PLUS value
        | value PLUS arithmetic
        | value MINUS value
        | value MINUS arithmetic
        | value EXPO value
        | value EXPO arithmetic
        | value MULT value
        | value MULT arithmetic
        | value DIV value
        | value DIV arithmetic
        | value MODULO value
        | value MODULO arithmetic
        """
        line = p.lineno(2)
        index = p.lexpos(2)

    def p_comparation(self, p):
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
        line = p.lineno(2)
        index = p.lexpos(2)

    def p_comparations(self, p):
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
        line = p.lineno(2)
        index = p.lexpos(2)

    def p_assignment(self, p):
        """assignment : ID ASSIGN ID
        | ID ASSIGN NIL
        | ID ASSIGN struc
        | ID ASSIGN literal
        | ID ASSIGN arithmetic
        """
        p[0] = p[2]
        line = p.lineno(2)
        index = p.lexpos(2)

    def p_assignment_operations(self, p):
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
        line = p.lineno(2)
        index = p.lexpos(2)

    def p_func(self, p):
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
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_else(self, p):
        """else : ELSE boolean statements
        | ELSE comparation statements
        | ELSE comparations statements
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_elsif(self, p):
        """elsif : ELSIF boolean statements
        | ELSIF comparation statements
        | ELSIF comparations statements
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_elses(self, p):
        """elses : else
        | elsif elses
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_contol_if(self, p):
        """control : IF boolean statements END
        | IF comparation statements END
        | IF comparations statements END
        | IF boolean statements elses END
        | IF comparation statements elses END
        | IF comparations statements elses END
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_control_unless(self, p):
        """control : UNLESS boolean COLON statements END
        | UNLESS comparation COLON statements END
        | UNLESS comparations COLON statements END
        | UNLESS boolean statements elses END
        | UNLESS comparation statements elses END
        | UNLESS comparations statements elses END
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_when(self, p):
        """when : WHEN literal
        | WHEN literal THEN
        | WHEN comparation
        | WHEN comparations
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_whens(self, p):
        """whens : when
        | when whens
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_control_case(self, p):
        """control : CASE ID whens else END
        | CASE ID whens END
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_control_while(self, p):
        """control : WHILE boolean DO statements END
        | WHILE comparation DO statements END
        | WHILE comparations DO statements END
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_element(self, p):
        """element : ID
        | STRING
        | boolean
        | numeric
        | range
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_elements(self, p):
        """elements : element
        | element COMMA elements
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_array(self, p):
        """array : L_BRACKET literals R_BRACKET
        | L_BRACKET ids R_BRACKET
        | L_BRACKET elements R_BRACKET
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_arrays(self, p):
        """arrays : array
        | array COMMA arrays
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_struc(self, p):
        """struc : strucMatrix
        | strucSet
        | strucHash
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_strucMatrix(self, p):
        "strucMatrix : MATRIX L_BRACKET arrays R_BRACKET"
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_strucSet(self, p):
        """strucSet : SET PERIOD NEW
        | SET PERIOD NEW L_PAREN R_PAREN
        | SET PERIOD NEW L_PAREN array R_PAREN
        | SET array
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_strucHash(self, p):
        """strucHash : HASH PERIOD NEW
        | HASH PERIOD NEW L_BRACE R_BRACE
        | HASH PERIOD NEW L_BRACE hashelems R_BRACE
        | HASH array
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_hashelem_rocket(self, p):
        """hashelem : COLON ID RW_DOUBLE_ARROW literal
        | ID COLON literal
        | STRING COLON literal
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_hashelems(self, p):
        """hashelems : hashelem COMMA hashelem
        | hashelem COMMA hashelems
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_range(self, p):
        """range : L_PAREN INTEGER ELLIPSIS INTEGER R_PAREN
        | L_PAREN INTEGER DOUBLE_PERIOD INTEGER R_PAREN
        | INTEGER ELLIPSIS INTEGER
        | INTEGER DOUBLE_PERIOD INTEGER
        | L_PAREN STRING ELLIPSIS STRING
        | L_PAREN STRING DOUBLE_PERIOD STRING
        | STRING ELLIPSIS STRING
        | STRING DOUBLE_PERIOD STRING
        """
        line = p.lineno(0)
        index = p.lexpos(0)

    def p_error(self, p):
        if p:
            print(f"Invalid Syntax : {p.type}, line {p.line}, pos {p.index}")
        else:
            print("Invalid Syntax EOF")

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, debug=1)

    def test(self, data):
        self.temp_out = StringIO() # Redirigir la salida estándar a un objeto StringIO
        with redirect_stdout(self.temp_out):
            self.parser.parse(data)
        return self.temp_out.getvalue() # Obtener el valor impreso



def get_title():
    return f"""
Syntactic Analysis
{('-') * 46}
"""


def yacc_data(data):
    parser = MyYacc()
    printing_data = get_title()
    result = parser.test(data)
    if result is not None:
        printing_data += f"{result}"
    return printing_data


def yacc_shell():
    parser = MyYacc()

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
        result = parser.test(statement)
        if result is not None:
            print(result)


def yacc_file(file_path):
    parser = MyYacc()

    printing_data = get_title()
    with open(file_path, mode="r", encoding="utf8") as data:
        data_lines = data.readlines()
        for line in data_lines:
            result = parser.test(line)
            if result is not None:
                printing_data += f"{result}"
    return printing_data
