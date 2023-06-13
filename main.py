import ply.lex as lex


#Algoritmo 1:
"""
def insertion_sort(array_datos)
    for i in 1...(array_datos.length)  # Step 1
        j = i # Step 2
        while j > 0 # Step 3
            if array_datos[j-1] > array_datos[j] # Step 4
                temp = array_datos[j]
                array_datos[j] = array_datos[j-1]
                array_datos[j-1] = temp
            else
                break
            end
            j = j - 1 # Step 5
        end
    end
    return array_datos
end
"""

#Algoritmo 2
"""
def merge_sort(array_datos)
  if array_datos.length <= 1
    return array_datos
  end
  array_size = array_datos.length
  middle = (array_datos.length / 2).round
  left_side = array_datos[0...middle]
  right_side = array_datos[middle...array_size]
  sorted_left = merge_sort(left_side)
  sorted_right = merge_sort(right_side)
  merge(array_datos, sorted_left, sorted_right)
  return array_datos
end

def merge(array_datos, sorted_left, sorted_right)
  left_size = sorted_left.length
  right_size = sorted_right.length
  array_pointer = 0
  left_pointer = 0
  right_pointer = 0
  while left_pointer < left_size && right_pointer < right_size
    if sorted_left[left_pointer] < sorted_right[right_pointer]
      array_datos[array_pointer] = sorted_left[left_pointer]
      left_pointer+=1
    else
      array_datos[array_pointer] = sorted_right[right_pointer]
      right_pointer+=1
    end
    array_pointer+=1
  end
  while left_pointer < left_size
      array_datos[array_pointer] = sorted_left[left_pointer]
      left_pointer+=1
      array_pointer+=1
  end
  while right_pointer < right_size
     array_datos[array_pointer] = sorted_right[right_pointer]
     right_pointer+=1
     array_pointer+=1
  end
  return array_datos
end
"""



#Algoritmo 3

"""
nombre= 'Xavier'
Apellido= "Pauta"
numeros= [1,2,3,4 ,5 ]
datos= ={ "Nombre"=>'Xavier Pauta' , edad: 21}

student1 = {
  name: "Juan",
  grades: {
    "Matemáticas" => 95,
    "Ciencias" => 87,
    "Historia" => 92,
    "Inglés" => 88
  }
}

edad= 23
case edad
when 10
    puts 'a'
when 15
    puts 'b'
else
    puts 'c'
end
"""

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
	'end': 'END',
    'case': 'CASE',
    'when': 'WHEN'
}

 #Sequencia de tokens, puede ser lista o tupla
tokens = (
		'TRIDOT',
		'DUODOT',
		'DOT',
        'DOTDOT',
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
		'AMPERSAND',
  'ID',
    'HASHROCKET',
    'LKEY', 'RKEY' , 'STRING'
) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_TRIDOT = r'\.\.\.'
t_DUODOT = r'\.\.'
t_DOT = r'\.'
t_EQCOMP = r'=='
t_COMMA = r'\,'
t_FLOAT = r'-?\d+\.[^.\d]+'
t_INT = r'-?\d+'
t_HASHROCKET= r'\=\>'
t_EQUALS = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LESSTH = r'\<'
t_GREATH = r'\>'
t_LKEY= r'\{'
t_RKEY= r'\}'
t_AMPERSAND = r'\&'
t_DOTDOT= r':'
 #Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# Valida si es una variable o palabra reservada
def t_ID(t):
  r'[a-zA-Z_]+\w*'
  t.type = reserved.get(t.value,'ID')
  return t

def t_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
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
  #caja_resultados.insert('1.0', "Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 
 #Contruir analizador
lexer = lex.lex()

#Testeando
data = """ """
 
 #Datos de entrada
#lexer.input(data)
 
 # Tokenizador
# while True:
#   tok = lexer.token()
#   if not tok:
#     break      #Rompe
#   print(tok)


from tkinter import *

root = Tk()
caja_resultados= Text(root)
caja_resultados.config(bd=0, padx=6, pady=4,font=("JetBrains Mono",12) ,
             insertbackground='white',spacing1='4',highlightthickness=2,
             insertborderwidth=10, background='black', fg='white',highlightbackground='#AEACAC',highlightcolor='#FFFFFF')
caja_resultados.grid(row=1, column=4,padx=10,sticky="w", columnspan=2)


def mostrarDatosLex():
    contenido= caja_codigo.get(1.0, 'end-1c')
    lexer.input(contenido)
    texto=[]
    for token in lexer:
        texto.append(str(token))
    texto= '\n'.join(texto)
    caja_resultados.delete('1.0','end')
    caja_resultados.insert('1.0', texto)


def borrarDatos():
    caja_codigo.delete("1.0","end")
    caja_resultados.delete("1.0", "end")


root.title("Mi editor")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)



#----------------------------Logo-------------------------#
logo = PhotoImage(file="imgs/ruby.png")
logo_label= Label(root, image=logo, bd=0)
logo_label.grid(row=0, column=1,columnspan=1, sticky="s")
#---------------------------------------------------------#


resultado= Label(root, font=("JetBrains Mono",24) ,text='Resultados', fg='white', background='black')
resultado.grid(row=0, column=4, columnspan=2)



#------------------------------Editor de texto------------------------------------#
caja_codigo = Text(root)
caja_codigo.config(bd=0, padx=6, pady=4,font=("JetBrains Mono",12) ,
             insertbackground='white',spacing1='4',highlightthickness=2,
             insertborderwidth=10,background='black', fg='white',highlightbackground='#AEACAC',highlightcolor='#FFFFFF')
caja_codigo.grid(row=1, column=0, columnspan=3,padx=10,sticky="n")
#-----------------------------------------------------------------------------------#


#------------------------------Resultados------------------------------------#

#-----------------------------------------------------------------------------------#


#------------------------------Boton Run-----------------------------------#
lexico = PhotoImage(file="imgs/run.png")
lexico_button= Button(root, relief='flat', padx=0,pady=0, command=mostrarDatosLex,image=lexico, bg='black',activeforeground='black',activebackground='black')
lexico_button.grid(row=2, column=0, pady=10,padx=10)



#------------------------------------------------------------------------------------#
delete = PhotoImage(file="imgs/delete.png")
delete_button= Button(root, relief='flat', padx=0, pady=0, command=borrarDatos,image=delete, bg='black',activeforeground='black',activebackground='black')
delete_button.grid(row=2, column=2, pady=10, sticky='s')


integrantes_label=Label(root, text='Integrantes:  ○ Nicolas Plaza  ○ Oscar Sanchez ○ Xavier Pauta',font=("JetBrains Mono",14), background='black',fg='white')
integrantes_label.grid(row=2, column=4)

root.configure(bg='black')
root.mainloop()