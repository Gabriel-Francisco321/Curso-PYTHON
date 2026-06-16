#
# Listas são coleções de valores
# As listas em python podem possuir diferentes tipos de dados
# As mesmas funcionalidades de fatiamento das strings se aplicam as listas.
# As listas podem ser alteradas a qualquer momento

# As buscas dentro de uma lista se fazem usando um indice, e podem ser 
#   feitas de ordem crescente (com indices positivos: 0 (primeiro), 1 (segundo), 2 (terceiro), ...) 
#   ou decrescente (com indices negativos: -1 (último), -2 (penultimo), -3 (antepenultimo), ...)

# Em python, ao fazermos a atribuição de uma lista a uma variável 
#   nós estamos a dar a essa variável o acesso ao objecto list, 
#   isso significa que se alterarmos a variável, a lista original também será alterada e vise-e-versa
# #

lista = [1, 2, 3, 4, 5, 6, 7, 8]

# Fatiamento da lista
meia_lista = lista[:4]

# Atribuição da lista a uma variável
mesma_lista = lista

print (lista)

# Sobre escrição de parte da lista
lista [4:8] = ['a', 'b', 'c', 'd']

print (meia_lista)

# Apresenta o mesmo que lista
print (mesma_lista)

mesma_lista [-2:] = []

print (lista)
print (len(lista))

# Adição de um novo item no final da lista
lista.append('c')

print (mesma_lista)

# Concatenação de listas

lista2 = lista + ['d', 'e']

print (lista2)