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


from collections import deque


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

#
# Outros métodos de Listas
# =====================================================================
# #

# extend([iterable]) - Adiciona os elementos de uma lista a outra lista
lista.extend(['d', 'e'])

# insert(index, value) - Adiciona um elemento em uma posição específica da lista
lista.insert(0, 'z')

# remove(value) - Remove o primeiro elemento da lista que corresponde ao valor especificado
lista.remove('z')

# pop(index) - Retorna o elemento da lista que está na posição especificada e o remove da lista
lista.pop(0)

# clear() - remove todos os elementos da lista
lista.clear()

# sort(key=None, reverse=False) - Ordena os elementos da lista, o parametro key é uma função que recebe um elemento da lista e retorna um valor que será usado para ordenar a lista, o parâmetro reverse indica se a lista será ordenada de forma crescente ou decrescente
lista = [3, 1, 4, 2]
lista.sort()

# count(value) - Retorna o número de vezes que um elemento aparece na lista
print(lista.count(2))

# copy() - Retorna uma cópia da lista, a cópia é uma nova lista, então alterações na cópia não afetam a lista original
lista_copia = lista.copy()


#
# Filas em Python
# ============================================================== #
# Utilizando a classe collections.deque, podemos criar uma fila em Python. A classe deque é uma lista que permite adicionar e remover elementos de ambos os lados da lista.



fila = deque([1, 2, 3, 4, 5])
fila.append(6)  # Adiciona um elemento no final da fila
fila.popleft()  # Remove e retorna o primeiro elemento da fila


#
# Compreensão de Listas
# ============================================================== #
# A compreensão de listas é uma forma de criar listas em Python de maneira legível com base em expressões.

lista = [x for x in range(10) if x % 2 == 0] # Cria uma lista com os números pares de 0 a 9


#
# Iterando sobre uma lista.
# ============================================================== #

# usando a função enumerate() podemos iterar sobre uma lista e obter o índice e o valor de cada elemento da lista.  
for i, item in enumerate(lista):
    print(i, item)

# Podemos usar a função zip() para iterar sobre duas ou mais listas ao mesmo tempo, retornando uma tupla com os elementos correspondentes de cada lista.
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
for item1, item2 in zip(lista1, lista2):
    print(f"{item1} => {item2}")