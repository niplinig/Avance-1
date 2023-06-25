#!/usr/bin/env python

# ----------------------------------
# main.py
#
# Analizador léxico de python
# ----------------------------------

import ply.lex as lex
from yachalk import chalk

# Diccionario de palabras reservadas

reserved = {
    "array": "ARRAY",
    "while": "WHILE",
    "def": "DEF",
    "for": "FOR",
    "if": "IF",
    "return": "RETURN",
    "in": "IN",
    "else": "ELSE",
    "break": "BREAK",
    "end": "END",
    "case": "CASE",
    "when": "WHEN",
    "class": "CLASS",
    "super": "SUPER",
    "elsif": "ELSIF",
    "begin": "BEGIN",
    "self": "SELF",
    "true": "TRUE",
    "false": "FALSE",
    "then": "THEN",
    "until": "UNTIL",
    "retry": "RETRY",
    "nil": "NIL",
    "or": "OR",
    "and": "AND",
    "unless": "UNLESS",
    "ensure": "ENSURE",
    "next": "NEXT",
}

# Secuencia de tokens

tokens = (
    "TRIDOT",
    "DUODOT",
    "DOT",
    "COMMENT",
    "EQCOMP",
    "EQUALS",
    "FLOAT",
    "INT",
    "PLUS",
    "PLUSEQ",
    "MINUS",
    "MINUSEQ",
    "EXPON",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "LBRAKET",
    "RBRAKET",
    "LESSTH",
    "LESSEQTH",
    "GREATEQTH",
    "GREATH",
    "COMMA",
    "AMPERS",
    "ID",
    "STRING",
    "AT",
    "DOLLARSGN",
    "UNDERSCR",
    "LBRACE",
    "RBRACE",
    "SEMICOLON",
    "COLON",
    "PIPE",
    "MODULE",
    "TILDE",
    "BOOLAND",
    "BOOLOR",
) + tuple(reserved.values())

# Expresiones regulares para cada token

t_ignore = " \t"
t_TRIDOT = r"\.\.\."
t_DUODOT = r"\.\."
t_FLOAT = r"\.[0-9]+"
t_DOT = r"\."
t_EQCOMP = r"=="
t_INT = r"[0-9]+"
t_PLUSEQ = r"\+="
t_PLUS = r"\+"
t_MINUSEQ = r"\-="
t_MINUS = r"\-"
t_EXPON = r"\*\*"
t_TIMES = r"\*"
t_COLON = r":"
t_UNDERSCR = r"\_"
t_BOOLAND = r"\&\&"
t_AMPERS = r"\&"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRAKET = r"\["
t_RBRAKET = r"\]"
t_GREATEQTH = r">="
t_LESSEQTH = r"<="
t_LESSTH = r"<"
t_GREATH = r">"
t_COMMA = r","
t_AT = r"@"
t_DOLLARSGN = r"\$"
t_LBRACE = r"{"
t_RBRACE = r"}"
t_SEMICOLON = r";"
t_BOOLOR = r"\|\|"
t_PIPE = r"\|"
t_MODULE = r"%"
t_TILDE = r"~"
t_EQUALS = r"="

# Número de líneas


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Nombre de Variable (evitar palabras reservadas)


def t_ID(t):
    r"[a-zA-Z_]+[a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")
    return


def t_STRING(t):
    r"(\'[^\']*\'|\"[^\"]*\")"
    return t


def t_COMMENT(t):
    r"\#.*"
    pass


def t_error(t):
    print(f"Componente léxico no reconocido {t.value[0]}")
    t.lexer.skip(1)


def main():
    print(chalk.bold.black.bg_green_bright("\nAnalizador Léxico\n"))
    data = open("data.txt", mode="r", encoding="utf-8")
    data_string = data.read()
    lexer = lex.lex()
    lexer.input(data_string)

    styled_pipe = chalk.bold.black("|")
    header_text = f"{styled_pipe} Token type {styled_pipe} Token value {styled_pipe} Line num {styled_pipe} Position {styled_pipe}"
    print(header_text)
    print(" ", chalk.bold.black("-") * 46)
    for tok in lexer:
        print(
            f"{styled_pipe}{tok.type}{' '*(12 - len(tok.type))}{styled_pipe}{tok.value}{' '*(13 - len(tok.value))}{styled_pipe}{tok.lineno}{' '*(10 - len(str(tok.lineno)))}{styled_pipe}{tok.lexpos}{' '*(10 - len(str(tok.lexpos)))}{styled_pipe}"
        )

    data.close()


if __name__ == "__main__":
    main()
