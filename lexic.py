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
    "not": "NOT",
    "new": "NEW",
    "do": "DO",
    "Set": "SET",
    "Hash": "HASH",
    "Matrix": "MATRIX",
}

# Secuencia de tokens

tokens = (
    "TRIDOT",
    "DUODOT",
    "DOT",
    "COMMENT",
    "EQCOMP",
    "EQUALS",
    "NOTEQ",
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
    "RAT",
    "COMPX",
    "ROCKET",
) + tuple(reserved.values())

# Expresiones regulares para cada token

t_ignore = " \t"
t_TRIDOT = r"\.\.\."
t_DUODOT = r"\.\."
t_DOT = r"\."
t_EQCOMP = r"=="
t_INT = r"[0-9]+"
t_PLUSEQ = r"\+="
t_PLUS = r"\+"
t_MINUSEQ = r"\-="
t_MINUS = r"\-"
t_EXPON = r"\*\*"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
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
t_ARROW = r"->"
t_ROCKET = r"=>"
t_NOTEQ = r"\!="
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
t_RAT = r"[1-9]+\/[1-9]+r"
t_COMPX = r"([0-9]*\.[0-9]+ri|[0-9]*\.[0-9]+ir)"

# Número de líneas


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Nombre de Variable (evitar palabras reservadas)


def t_ID(t):
    r"[a-zA-Z_]+\w*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_STRING(t):
    r"(\'[^\']*\'|\"[^\"]*\")"
    return t


def t_FLOAT(t):
    r"([0-9]*\.[0-9]+|[0-9]*\.[0-9]e-?[1-9]+)"
    return t


def t_COMMENT(t):
    r"\#.*"
    pass


def t_error(t):
    print(f"Componente léxico no reconocido {t.value[0]}")
    t.lexer.skip(1)


spp = chalk.bold.black("|")


def print_title():
    print(chalk.bold.black.bg_green_bright("\nAnalizador Léxico\n"))
    header_text = (
        f"{spp} Token type {spp}  Token value  {spp} Line num {spp} Position {spp}"
    )
    print(header_text)
    print(" ", chalk.bold.black("-") * 46)


# Building lexer

lexer = lex.lex()


def lex_data(data):
    print_title()
    lexer.input(data)
    for tok in lexer:
        print(
            f"{spp}{tok.type}{' '*(12-len(tok.type))}{spp}{tok.value}{' '*(15-len(tok.value))}{spp}{tok.lineno}{' '*(10-len(str(tok.lineno)))}{spp}{tok.lexpos}{' '*(10-len(str(tok.lexpos)))}{spp}"
        )


def lex_file(file_path):
    print_title()
    with open(file_path, mode="r", encoding="utf8") as data:
        data_lines = data.readlines()
        for line in data_lines:
            lexer.input(line)
            for tok in lexer:
                print(
                    f"{spp}{tok.type}{' '*(12-len(tok.type))}{spp}{tok.value}{' '*(15-len(tok.value))}{spp}{tok.lineno}{' '*(10-len(str(tok.lineno)))}{spp}{tok.lexpos}{' '*(10-len(str(tok.lexpos)))}{spp}"
                )
    data.close()
