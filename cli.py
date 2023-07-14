#!/usr/bin/env python

# ==============================================
#
# cli.py.py
#
# Command Line Interface CLI
#
# ==============================================

import argparse
from lexical import lex_data, lex_file
from semantic import yacc_shell, yacc_file, yacc_data
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

    group.add_argument("-ld", "--lex_data", help="Data to tokenize", type=str)

    group.add_argument("-yd", "--yacc_data", help="Data to analyse", type=str)

    group.add_argument("-s", "--shell", help="Syntax Shell", action="store_true")

    args = parser.parse_args()

    if args.yacc_file:
        print(yacc_file(args.yacc_file))
    elif args.lex_file:
        print(lex_file(args.lex_file))
    elif args.lex_data:
        print(lex_data(args.lex_data))
    elif args.yacc_data:
        print(yacc_data(args.yacc_data))
    elif args.shell:
        yacc_shell()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
