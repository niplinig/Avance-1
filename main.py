import ply.lex as lex

#Crear los tokens para la siguiente sintaxis

"""
def insertion_sort(array)
    for i in 1...(array.length)  # Step 1
        j = i # Step 2
        while j > 0 # Step 3
            if array[j-1] > array[j] # Step 4
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else
                break
            end
            j = j - 1 # Step 5
        end
    end
    return array
end
"""

#SELECT * FROM Tabla
#SELECT campo1, campo2 from Tabla1 where campo==1
#SELECT campo1 as cedula from Datos where provincia<>"7"
#print(consulta)
#DELETE FROM datos WHERE id>1000
#print("SELECT * FROM Tabla")

#Diccionario de palabras reservadas
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
	'end': 'END'
}

 #Sequencia de tokens, puede ser lista o tupla
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
		'LBREAK',
		'RBREAK',
		'LESSTH',
		'GREATH',
		'COMMA',
  'ID',
) + tuple(reserved.values())
 
 #Exp Regulares para tokens de símbolos
t_TRIDOT = r'\.\.\.'
t_DUODOT = r'\.\.'
t_DOT = r'\.'
t_EQCOMP = r'=='
t_COMMA = r'\,'
t_FLOAT = r'-?\d+\.[^.\d]+'
t_INT = r'-?\d+'
t_EQUALS = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LESSTH = r'\<'
t_GREATH = r'\>'
 
 #Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# Valida si es una variable o palabra reservada
def t_ID(t):
  r'[a-zA-Z_]+\w*'
  t.type = reserved.get(t.value,'ID')
  return t

t_LBREAK = r'\['
t_RBREAK = r'\]'

 # Ignorar lo que no sea un token en mi LP
t_ignore  = ' \t'

def t_COMMENT(t):
	r'\#.*'
	pass
 
 #Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 
 #Contruir analizador
lexer = lex.lex()

#Testeando
data = """
def insertion_sort(array)
    for i in 1...(array.length)  # Step 1
        j = i # Step 2
        while j > 0 # Step 3
            if array[j-1] > array[j] # Step 4
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else
                break
            end
            j = j - 1 # Step 5
        end
    end
    return array
end
"""
 
 #Datos de entrada
lexer.input(data)
 
 # Tokenizador
while True:
  tok = lexer.token()
  if not tok: 
    break      #Rompe
  print(tok)