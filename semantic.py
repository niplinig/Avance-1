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

    precednece = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIV'),
    )

    start = "init"

    def p_init(self, p):
        "init : statement"

    def p_statement(self, p):
        """statement : assignment
        | comparations
        | function
        """

    def p_funcBody(self, p):
        """funcBody : assignment
        | comparations
        """

    def p_funcBodys(self, p):
        """funcBodys : 
        """

    def p_boolean(self, p):
        """boolean : TRUE
        | FALSE
        """

    def p_numeric(self, p):
        """numeric : FLOAT
        | INTEGER
        """

    def p_literal(self, p):
        """literal : STRING
        | boolean
        | numeric
        """

    def p_ids(self, p):
        """ids : ID
        | ID COMMA ids
        """

    def p_nvalue(self, p): # numeric value
        """nvalue : numeric
        | ID
        """

    def p_value(self, p): # both numeric
        """value : STRING
        | numeric
        | ID
        """    

    def p_arithOp(self, p):
        """arithOp : PLUS
        | MINUS
        | EXPO
        | MULT
        | DIV
        | MODULO
        """

    def p_arithmetic(self, p):
        """arithmetic : nvalue arithOp nvalue
        | nvalue arithOp arithmetic
        """

    def p_assignment(self, p):
        """assignment : ID ASSIGN ID
        | ID ASSIGN NIL
        | ID ASSIGN literal
        | ID ASSIGN arithmetic
        """

    def p_assignOp(self, p):
        """assignOp : ADD_ASSIGN
        | SUBS_ASSIGN
        | MULT_ASSIGN
        | DIV_ASSIGN
        | MOD_ASSIGN
        """

    def p_assignment_operations(self, p):
        """assignment : ID assignOp value
        """ 

    def p_comparator(self, p):
        """comparator : EQUAL
        | NOT_EQ
        | LT_OR_EQ
        | GT_OR_EQ
        | LESS_THAN
        | GREATER_THAN
        """

    def p_logicOp(self, p):
        """logicOp : AND
        | LOGIC_AND
        | OR
        | LOGIC_OR
        """

    def p_comparation(self, p):
        """comparation : STRING comparator STRING
        | nvalue comparator nvalue
        """

    def p_comparations(self, p):
        """comparations : comparation
        | comparation logicOp comparation
        """    

    def p_function(self, p):
        """function : DEF ID L_PAREN ids R_PAREN funcBody END
        | DEF ID L_PAREN R_PAREN funcBody END
        | DEF ID funcBody END
        | DEF ID L_PAREN ids R_PAREN funcBody RETURN ID END
        | DEF ID L_PAREN R_PAREN funcBody RETURN ID END
        | DEF ID funcBody RETURN ID END
        | DEF ID L_PAREN ids R_PAREN funcBody RETURN literal END
        | DEF ID L_PAREN R_PAREN funcBody RETURN literal END
        | DEF ID funcBody RETURN literal END
        """

    def p_error(self, p):
        if not p:
            print("Invalid Syntax End of File (EOF)")
            return

        if p is None or p.type == 'END':
            next
        else:
            print(f"{' '*(18 - len(p.type))}{p.type}{' '*(18 - len(p.type))}{' '*(13 - len(str(p.lineno)))}{p.lineno}{' '*(13 - len(str(p.lineno)))}{' '*(10 - len(str(p.lexpos)))}{p.lexpos}{' '*(10 - len(str(p.lexpos)))}")
             
        while True:
            tok = self.parser.token()
            if tok is None or tok.type == 'END':
                break
            print(f"{' '*(18 - len(tok.type))}{tok.type}{' '*(18 - len(tok.type))}{' '*(13 - len(str(tok.lineno)))}{tok.lineno}{' '*(13 - len(str(tok.lineno)))}{' '*(10 - len(str(tok.lexpos)))}{tok.lexpos}{' '*(10 - len(str(tok.lexpos)))}")
        self.parser.restart()
            

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, debug=1)

    def test(self, data):
        self.temp_out = StringIO() # Redirigir la salida estándar a un objeto StringIO
        with redirect_stdout(self.temp_out):
            self.parser.parse(data, tracking=True)
        return self.temp_out.getvalue() # Obtener el valor impreso



def get_title():
    return f"""
Syntactic Analysis
|    Token type    | Line number | Position |
{('-') * 108}
"""


def yacc_data(data):
    parser = MyYacc()
    return get_title() + f"{parser.test(data)}"


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
    with open(file_path, mode="r", encoding="utf8") as data:
        return get_title() + f"{parser.test(data.read())}"
