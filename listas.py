#
# Listas em Python
# ============================================================== #

#
# Listas são coleções de valores
# As listas em python podem possuir diferentes tipos de dados
# As mesmas funcionalidades de fatiamento das strings se aplicam as listas.
# As listas podem ser alteradas a qualquer momento

# As buscas dentro de uma lista se fazem usando um indice, e podem ser 
#   feitas de ordem crescente (com indices positivos: 0 (primeiro), 1 (segundo), 2 (terceiro), ...) 
#   ou decrescente (com indices negativos: -1 (último), -2 (penultimo), -3 (antepenultimo), ...)


lista = [1, 2, 3, 4, 5, 6, 7, 8]

# Fatiamento da lista
meia_lista = lista[:4]

print (lista)

# Sobre escrição de parte da lista
lista [4:8] = ['a', 'b', 'c', 'd']

print (meia_lista)

# A função len() retorna o comprimento da lista
print (len(lista))

# Adição de um novo item no final da lista
lista.append('c')

print (lista)

# Concatenação de listas
lista2 = lista + ['d', 'e']

print (lista2)

# Em python, ao fazermos a atribuição de uma lista a uma variável 
#   nós estamos a dar a essa variável o acesso ao objecto list, 
#   isso significa que se alterarmos a variável, a lista original também será alterada e vise-e-versa
# #
mesma_lista = lista

# Apresenta o mesmo que lista
print (mesma_lista)

mesma_lista [-2:] = []

# O penultimo e o último elementos da lista foram removidos, e como a mesma_lista é 
#   uma referência para a lista original, a lista original também foi alterada.
print (lista)

# A palavra reservada in é utilizada para verificar se um elemento está contido dentro de uma lista.
print("a" in lista)