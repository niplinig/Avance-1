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
        ('left', 'L_PAREN', 'R_PAREN'),
        ('left', 'L_BRACKET', 'R_BRACKET'),
        ('left', 'L_BRACE', 'R_BRACE'),
    )

    start = "init"

    def p_init(self, p):
        "init : statements"

    def p_statement(self, p):
        """statement : assignment
        | comparations
        | function
        | loop
        | conditional
        | print
        | classMethod
        | classField
        | struc
        | indexArray
        """

    def p_statements(self, p):
        """statements : statement
        | statement statements
        """

    def p_funcBody(self, p):
        """funcBody : assignment
        | comparations
        | loop
        | conditional
        | print
        | classMethod
        | classField
        | struc
        | indexArray
        """

    def p_funcBodys(self, p):
        """funcBodys : funcBody
        | funcBody funcBodys
        """

    def p_condiBlock(self, p):
        """condiBlock : assignment
        | comparations
        | conditional
        | loop
        | print
        | classMethod
        | classField
        | struc
        | indexArray
        | BREAK
        """

    def p_condiBlocks(self, p):
        """condiBlocks : condiBlock
        | condiBlock condiBlocks
        """

    def p_loopBlock(self, p):
        """loopBlock : assignment
        | comparations
        | conditional
        | print
        | loop
        | classMethod
        | classField
        | struc
        | indexArray
        | BREAK
        """

    def p_loopBlocks(self, p):
        """loopBlocks : loopBlock
        | loopBlock loopBlocks
        """

    def p_boolean(self, p):
        """boolean : TRUE
        | FALSE
        """

    def p_numeric(self, p):
        """numeric : FLOAT
        | INTEGER
        """

    def p_pointOp(self, p):
        """pointOp : ELLIPSIS
        | DOUBLE_PERIOD
        """

    def p_range(self, p):
        """range : L_PAREN INTEGER pointOp INTEGER R_PAREN
        | INTEGER pointOp INTEGER
        | L_PAREN STRING pointOp STRING R_PAREN
        | STRING pointOp STRING
        | L_PAREN ID pointOp ID R_PAREN
        | ID pointOp ID
        | INTEGER pointOp L_PAREN classField R_PAREN
        """

    def p_literal(self, p):
        """literal : STRING
        | boolean
        | numeric
        | range
        """

    def p_ids(self, p):
        """ids : ID
        | ID COMMA ids
        """

    def p_nvalue(self, p): # numeric value
        """nvalue : numeric
        | ID
        """

    def p_value(self, p): # literal + id
        """value : literal
        | ID
        """

    def p_values(self, p):
        """values : value
        | value COMMA values
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
        | ID ASSIGN struc
        | ID ASSIGN classField
        | indexArray ASSIGN value
        | indexArray ASSIGN indexArray
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
        | numeric comparator numeric
        | ID comparator value
        | indexArray comparator indexArray
        """

    def p_comparations(self, p):
        """comparations : comparation
        | comparation logicOp comparation
        | boolean logicOp boolean
        """

    def p_function(self, p):
        """function : DEF ID L_PAREN ids R_PAREN funcBodys END
        | DEF ID L_PAREN R_PAREN funcBodys END
        | DEF ID funcBodys END
        | DEF ID L_PAREN ids R_PAREN funcBodys RETURN ID END
        | DEF ID L_PAREN R_PAREN funcBodys RETURN ID END
        | DEF ID funcBodys RETURN ID END
        | DEF ID L_PAREN ids R_PAREN funcBodys RETURN literal END
        | DEF ID L_PAREN R_PAREN funcBodys RETURN literal END
        | DEF ID funcBodys RETURN literal END
        """

    def p_classMethod(self, p):
        """classMethod : ID L_PAREN values R_PAREN
        | ID L_PAREN R_PAREN
        """

    def p_classField(self, p):
        """classField : ID PERIOD ID
        """

    def p_else(self, p):
        """else : ELSE condiBlocks
        """

    def p_elsif(self, p):
        """elsif : ELSIF boolean condiBlocks
        | ELSIF comparations condiBlocks
        """

    def p_elses(self, p):
        """elses : else
        | elsif elses
        """

    def p_conditional_if(self, p):
        """conditional : IF boolean condiBlocks END
        | IF comparations condiBlocks END
        | IF boolean condiBlocks elses END
        | IF comparations condiBlocks elses END
        """

    def p_conditional_unless(self, p):
        """conditional : UNLESS boolean condiBlocks END
        | UNLESS comparations condiBlocks END
        | UNLESS boolean condiBlocks elses END
        | UNLESS comparations condiBlocks elses END
        """

    def p_print(self, p):
        """print : PUTS value
        | PRINT value
        """

    def p_when(self, p):
        """when : WHEN value STRING
        | WHEN value THEN STRING
        | WHEN value condiBlocks
        | WHEN value THEN condiBlocks
        """

    def p_whes(self, p):
        """whens : when
        | when whens
        """

    def p_conditional_case(self, p):
        """conditional : CASE ID whens else END
        | CASE ID whens END
        """

    def p_loop_while(self, p):
        """loop : WHILE boolean loopBlocks END
        | WHILE comparations loopBlocks END
        | WHILE boolean DO loopBlocks END
        | WHILE comparations DO loopBlocks END
        """

    def p_loop_for(self, p):
        """loop : FOR ID IN range loopBlocks END
        | FOR ID IN range DO loopBlocks END
        | FOR ID IN ID loopBlocks END
        | FOR ID IN ID DO loopBlocks END
        """

    def p_struc(self, p):
        """struc : strucArray
        | strucSet
        | strucMatrix
        | strucHash
        """

    def p_indexArray(self, p):
        """indexArray : ID L_BRACKET ID R_BRACKET
        | ID L_BRACKET INTEGER R_BRACKET
        | ID L_BRACKET arithmetic R_BRACKET
        """

    def p_strucArray(self, p):
        """strucArray : L_BRACKET values R_BRACKET
        """

    def p_strucSet(self, p):
        """strucSet : SET PERIOD NEW
        | SET PERIOD NEW L_PAREN R_PAREN
        | SET PERIOD NEW L_PAREN strucArray R_PAREN
        | SET strucArray
        """

    def p_arrays(self, p):
        """arrays : strucArray
        | strucArray COMMA arrays
        """

    def p_strucMatrix(self, p):
        "strucMatrix : MATRIX L_BRACKET arrays R_BRACKET"


    def p_hashElem(self, p):
        """hashElem : COLON ID RW_DOUBLE_ARROW literal
        | ID RW_DOUBLE_ARROW literal
        | ID COLON literal
        | STRING COLON literal
        | STRING RW_DOUBLE_ARROW literal
        """

    def p_hashElems(self, p):
        """hashElems : hashElem
        | hashElem COMMA hashElems
        """

    def p_strucHash(self, p):
        """strucHash : L_BRACE R_BRACE
        | L_BRACE hashElems R_BRACE
        | HASH PERIOD NEW
        | HASH PERIOD NEW L_BRACE R_BRACE
        | HASH PERIOD NEW L_BRACE hashElems R_BRACE
        | HASH strucArray
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
