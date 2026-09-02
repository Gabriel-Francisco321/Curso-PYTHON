#
# Sequências
# ============================================================== #

# Listas, strings e tuplas são exemplos de sequências em python. 


# Tuplas
# -----------------------------------------------------

# tuplas são conjuntos de elementos que não podem ser alterados.

# tupla: (1, 2, 3) != lista: [1, 2, 3]

tupla = (1, 2, 3)
print(tupla)

# Desempacotamento de tuplas
a, b, c = tupla # para que isso funcione, a quantidade de variáveis deve ser igual a quantidade de elementos da tupla
print(a, b, c)


# Conjuntos
# -----------------------------------------------------

# Conjuntos são coleções não ordenadas de elementos únicos, ou seja, não podem conter elementos duplicados.
# Por não serem ordenados, não é possível acessar elementos de um conjunto por índice.

# Conjuntos são definidos com chaves {} ou com a função set().
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
# ou
conjunto2 = set([1, 2, 3, 4, 5])
print(conjunto2)

# É possível realizar operações matemáticas com conjuntos, como união, interseção e diferença.
a = set('abracadabra')
b = set('alacazam')

print(a - b)    # letras em a, mas não em b
# resultado {'r', 'd', 'b'}
print(a | b)    # letras em a ou em b ou ambos
# resultado {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)    # letras em ambos a e b
# resultado {'a', 'c'}
print(a ^ b)    # letras em a ou b, mas não em ambos
# resultado {'r', 'd', 'b', 'm', 'z', 'l'}


#
# Comparação de Sequências
# ========================================================= #

# Ao comparar duas sequências, os elementos são avaliados um a um.
# Se uma das sequências tever mais elementos que a outra, ela sera considerada maior. 
print((1, 2, 3) < (1, 2, 4)) # True
print((1, 2) < (1, 2, -1)) # True