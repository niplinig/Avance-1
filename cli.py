#!/usr/bin/env python

# ----------------------------------
# cli.py
#
# Interfaz de Línea de Comandos
# ----------------------------------

import argparse
from lexic import lex_data, lex_files
import pathlib


def main():
    parser = argparse.ArgumentParser(
        prog="LexRuby",
        description="Analizador léxico de Ruby",
        epilog="Trabajo en progreso",
    )

    parser.add_argument(
        "-f",
        "--files",
        help="Ruby text files",
        type=pathlib.Path,
        default="data.rb",
    )
    parser.add_argument("-d", "--data", help="Data to analyse", type=str)

    args = parser.parse_args()

    if args.files != "data.rb" and not args.data:
        lex_files(args.files)
    elif args.data:
        lex_data(args.data)
    else:
        pass


if __name__ == "__main__":
    main()
