#!/usr/bin/env python

# ==============================================
#
# lexical.py
#
# Lexical Analyser and tokenizer
#
# ==============================================

import ply.lex as lex

# ----------------------------------
#
#	Reserverd words or identifiers
#
# ----------------------------------

class MyLexer(object):

	reserved = {
		# Exceptions syntax
		"begin": "BEGIN", # Starts an exception handling block.
		"end": "END", # The end of a syntax block. Used by classes, modules, methods, exception handling and control expressions.

		# Control expression syntax
		"case": "CASE", # Starts a case expression.
		
		# Control expressions
		"if": "IF", # Used for if and modifier if statements.
		"unless": "UNLESS", # Used for unless and modifier unless statements.
		"then": "THEN", # Indicates the end of conditional blocks in control structures.
		"elsif": "ELSIF", # An alternate condition for an if expression.
		"else": "ELSE", # The unhandled condition in case, if and unless expressions. 
		
		"for": "FOR", # A loop that is similar to using the each method.
		"in": "IN", # Used to separate the iterable object and iterator variable in a for
		"next": "NEXT", # Skips the rest of the block.
		
		"while": "WHILE", # Creates a loop that executes while the condition is true.
		"do": "DO", # Starts a block.
		"break": "BREAK",
		"when": "WHEN", # A condition in a case expression.
		"until": "UNTIL", # Creates a loop that executes until the condition is true
		
		# Boolean and Nil Literals
		"true": "TRUE", # Boolean true. 
		"false": "FALSE", # Boolean false.
		"nil": "NIL", # A false value usually indicating “no value” or “unknown”.

		# Boolean opoerators
		"or": "OR", # Boolean or with lower precedence than ||
		"and": "AND", # Short-circuit Boolean and with lower precedence than &&
		"not": "NOT", # Inverts the following boolean expression. Has a lower precedence than !

		# Modules and classes syntax
		"class": "CLASS", # Creates or opens a class. 

		# Methods
		"super": "SUPER", # Calls the current method in a superclass.
		"self": "SELF", # The object the current method is attached to.
		"new": "NEW",

		# Method syntax
		"def": "DEF", # Defines a method. 
		"return": "RETURN", # Exits a method.
		
		# Exception handling
		"retry": "RETRY", # Retries an exception block. 
		"ensure": "ENSURE", # Starts a section of code that is always run when an exception is raised.

		# Data structure
		"array": "ARRAY", # An Array is an ordered, integer-indexed collection of objects, called elements.
		"Set": "SET", # Set implements a collection of unordered values with no duplicates. 
		"Hash": "HASH", # A Hash maps each of its unique keys to a specific value.
		"Matrix": "MATRIX", # The Matrix class represents a mathematical matrix.
	}

	# ----------------------------------
	#
	#	List of token names
	#
	# ----------------------------------

	tokens = (

		# Comparison Operators
		"EQUAL", # ==
		"NOT_EQ", # !=
		"GT_OR_EQ", # >=
		"LT_OR_EQ", # <=

		# Assignment Operators
		"ADD_ASSIGN", # +=
		"SUBS_ASSIGN", # -=
		"MULT_ASSIGN", # *=
		"DIV_ASSIGN", # /=
		"MOD_ASSIGN", # %=
		"RW_DOUBLE_ARROW", # =>
		"RW_ARROW", # ->
		"ASSIGN", # =

		# Logical Operators
		"LOGIC_NOT", # !
		"LOGIC_AND", # &&
		"LOGIC_OR", # ||
		
		# Arithmetic Operators
		"PLUS", # +
		"MINUS", # -
		"EXPO", # **
		"MULT", # *
		"DIV", # /
		"GREATER_THAN", # >
		"LESS_THAN", # <
		"MODULO", # %

		# Other Operators
		"ELLIPSIS", # ...
		"DOUBLE_PERIOD", # ..
		"PERIOD", # .
		"AMPERSAND", # &
		"AT_SIGN", # @
		"DOLLAR_SIGN",# $
		"UNDERSCORE", # _
		"VERTICAL_BAR", # |
		"TILDE", # ~

		# Separators
		"SEMICOLON", # ;
		"COLON", # :
		"COMMA", # ,

		# Delimiters
		"L_PAREN", # (
		"R_PAREN", # )
		"L_BRACE", # {
		"R_BRACE", # }
		"L_BRACKET", # [
		"R_BRACKET", # ]
		
		# Literals
		"COMPLEX", # 1+1i
		"RATIONAL", # 1/2r
		"FLOAT", # 0.5
		"INTEGER",	# 10
		"STRING", # "Hi" 'Hi'

		# Identifier
		"ID", # x, color, UP

		# Comment
		"LINE_COMMENT", # #...
		
	) + tuple(reserved.values())

	# ----------------------------------
	#
	#	Regex rules for tokens
	#
	# ----------------------------------

	# Comparison Operators
	t_EQUAL = r"=="
	t_NOT_EQ =  r"\!="
	t_GT_OR_EQ =  r">="
	t_LT_OR_EQ =  r"<="

	# Assignment Operators
	t_ADD_ASSIGN = r"\+="
	t_SUBS_ASSIGN = r"-="
	t_MULT_ASSIGN = r"\*="
	t_DIV_ASSIGN = r"/="
	t_MOD_ASSIGN = r"%="
	t_RW_DOUBLE_ARROW = r"=>"
	t_RW_ARROW = r"->"
	t_ASSIGN = r"="

	# Logical Operators
	t_LOGIC_NOT = r"\!"
	t_LOGIC_AND = r"&&"
	t_LOGIC_OR = r"\|\|"

	# Arithmetic Operators
	t_PLUS = r"\+"
	t_MINUS = r"-"
	t_EXPO = r"\*\*"
	t_MULT = r"\*"
	t_DIV = r"/"
	t_GREATER_THAN = r">"
	t_LESS_THAN = r"<"
	t_MODULO = r"%"

	# Other Operators
	t_ELLIPSIS = r"\.\.\."
	t_DOUBLE_PERIOD =  r"\.\."
	t_PERIOD = r"\."
	t_AMPERSAND = r"&"
	t_AT_SIGN = r"@"
	t_DOLLAR_SIGN = r"\$"
	t_UNDERSCORE = r"_"
	t_VERTICAL_BAR = r"\|"
	t_TILDE = r"~"

	# Separators
	t_SEMICOLON = r";"
	t_COLON = r":"
	t_COMMA = r","

	# Delimiters
	t_L_PAREN = r"\("
	t_R_PAREN = r"\)"
	t_L_BRACE = r"{"
	t_R_BRACE = r"}"
	t_L_BRACKET = r"\["
	t_R_BRACKET = r"\]"

	# Literals
	t_COMPLEX = r"([0-9]*\.[0-9]+ri|[0-9]*\.[0-9]+ir)"
	t_RATIONAL = r"[1-9]+/[1-9]+r"
	t_FLOAT = r"([0-9]*\.[0-9]+|[0-9]*\.[0-9]e-?[1-9]+)"
	t_INTEGER = r"[0-9]+"
	t_STRING = r"(\'[^\']*\'|\"[^\"]*\")"

	t_ignore = " \t"

	# ----------------------------------
	#
	#	Regex rules with action code
	#
	# ----------------------------------

	def t_newline(self, t):
		r"\n+"
		t.lexer.lineno += len(t.value)

	def t_LINE_COMMENT(self, t):
		r"\#.*"
		pass

	def t_ID(self, t):
		r"[a-zA-Z_]+\w*"
		t.type = self.reserved.get(t.value, "ID")
		return t

	def t_error(self, t):
		print(f"Illegal character {t.value[0]}")
		t.lexer.skip(1)

	def __init__(self, **kwargs):
		self.lexer = lex.lex(module=self, **kwargs, debug=1)

	def test(self, data):
		tokens = ""
		self.lexer.input(data)
		for tok in self.lexer:
			tokens += f"{' '*(18 - len(tok.type))}{tok.type}{' '*(18 - len(tok.type))}{' '*(17 - len(tok.value))}{tok.value}{' '*(17 - len(tok.value))}{' '*(13 - len(str(tok.lineno)))}{tok.lineno}{' '*(13 - len(str(tok.lineno)))}{' '*(10 - len(str(tok.lexpos)))}{tok.lexpos}{' '*(10 - len(str(tok.lexpos)))}\n"
		return tokens


def get_title():
	return f"""
Lexical Analysis
|    Token type    |   Token value   | Line number | Position |
{('-') * 108}
"""

# ----------------------------------
#
#	Build the lexer
#
# ----------------------------------

def lex_data(data):
    lexer = MyLexer()
    return get_title().join(lexer.test(data))

def lex_file(file_path):
    lexer = MyLexer()
    printing_data = get_title()
    with open(file_path, mode="r", encoding="utf8") as data:
        data_lines = data.readlines()
        for line in data_lines:
            printing_data += f"{lexer.test(line)}"
    return printing_data
