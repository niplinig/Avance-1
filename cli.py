#!/usr/bin/env python

# ----------------------------------
# cli.py
#
# Interfaz de Línea de Comandos
# ----------------------------------

import argparse
from lexic import lex_data, lex_file
from semtic import yacc_shell, yacc_file
import pathlib


def main():
    parser = argparse.ArgumentParser(
        prog="LexRuby",
        description="Analizador léxico de Ruby",
        epilog="Trabajo en progreso",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-lf", "--lex_file", help="Ruby text file", type=pathlib.Path)

    group.add_argument("-yf", "--yacc_file", help="Ruby text file", type=pathlib.Path)

    group.add_argument("-d", "--data", help="Data to analyse", type=str)

    group.add_argument("-s", "--shell", help="Syntax Shell", action="store_true")

    args = parser.parse_args()

    if args.yacc_file:
        yacc_file(args.yacc_file)
    elif args.lex_file:
        lex_file(args.lex_file)
    elif args.data:
        lex_data(args.data)
    elif args.shell:
        yacc_shell()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
