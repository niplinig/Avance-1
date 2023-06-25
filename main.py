#!/usr/bin/env python

from ply.lex import lex
from ply.yacc import yacc

# Diccionario de palabras reservadas

reserved = {
        'array': 'ARRAY',
        'while': 'WHILE',
        'def': 'DEF',
        'for': 'FOR',
        'if': 'IF',
        'return': 'RETURN',
        'in': 'IN',
        'else': 'ELSE',
        'break': 'BREAK',
        'end': 'END',
        'case': 'CASE',
        'when': 'WHEN',
        'class': 'CLASS',
        'super': 'SUPER',
        'elsif': 'ELSIF',
        'begin': 'BEGIN',
        'self': 'SELF',
        'true': 'TRUE',
        'false': 'FALSE',
        'then': 'THEN',
        'until': 'UNTIL',
        'retry': 'RETRY',
        'nil': 'NIL',
        'or': 'OR',
        'and': 'AND',
        'unless': 'UNLESS',
        'ensure': 'ENSURE',
        'next': 'NEXT'
        }

# Secuencia de tokens

tokens = (
        'TRIDOT',
        'DUODOT',
        'DOT',
        'COMMENT',
        'EQCOMP',
        'EQUALS',
        'FLOAT',
        'INT',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'LBRAKET',
        'RBRAKET',
        'LESSTH',
        'GREATH',
        'COMMA',
        'AMPERS',
        'ID',
        'STRING',
        'AT',
        'DOLLARSGN',
        'UNDERSCR',
        'HYPHEN',
        'LBRACE',
        'RBRACE',
        'SEMICOLON',
        'COLON',
        'PIPE',
        'MODULE',
        'TILDE'
        ) + tuple(reserved.values())

# Expresiones regulares para cada token

t_ignore = ' \t'

t_TRIDOT = r'\.\.\.'
t_DUODOT = r'\.\.'
t_FLOAT = r'\.[0-9]+'
t_DOT = r'\.'
t_COLON = r':'
t_UNDERSCR = r'_'
t_AMPERSAND = r'\&'

def main():
    print("Hello World!")

if __name__ == '__main__':
    main()
