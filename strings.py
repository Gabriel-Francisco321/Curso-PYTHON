#
# Strings em Python
# ============================================================== #

#
# Em python, strings são tratadas como listas de caracteres
# As strings em python são imutáveis, é impossível alterar um ou mais caracter da string. Sendo 
#    apenas possível criar novas estrings para isso
# Não existem caracteres em python, um caracter é apenas uma string de um só caracter.
# #


#Concatenação sem operador (Automática)
nome_completo = ('Gabriel Octávio '
                  'Luís Francisco')

#Fatiamento de string
nome1 = nome_completo[:7]
nome2 = nome_completo[8:15]
nome3 = nome_completo[16:20]
ultimo_nome = nome_completo[21:30]

#Concatenação usando o operador +
apelido = nome1[:3] + nome1[4]

print('\nnome completo: ' + nome_completo)

print('\nprimeiro nome: ' + nome1)
print('\nsegundo nome: ' + nome2)
print('\nterceiro nome: ' + nome3)
print('\nultimo nome: ' + ultimo_nome)

print('\napelido: ' + apelido)

# Multiplicação de strings
# É possível multiplicar uma string por um número inteiro, o que resulta na repetição da string o número
#      de vezes especificado.
print('\n3 apelidos: ' + 3 * apelido)

# String complexa
print ("""\
Algumas coisas para começar:
       1º blablabla
       2º blablablabla
""")

# template strings
# Ao utilizar f antes das aspas, podemos utilizar variáveis dentro da string, bastando para isso colocar 
#      o nome da variável entre chaves.
print (f'Olá, {nome1} {nome2} {nome3} {ultimo_nome}, seu apelido é {apelido}.')