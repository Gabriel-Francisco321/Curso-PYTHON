#
# Dicionários
# ============================================================== #

# Um dicionário é um confundo de pares chave-valor, semelhantes as estruturas JSON.
# Cada chave de um dicionário deve ser única e imutável.

# Dicionário: {'chave': 'valor'}
dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
print(dicionario)

# Acessando valores pelo nome da chave
print(dicionario['nome']) # Ou podemos acessar com o método get()
print(dicionario.get('idade')) # Se a chave não existir, retorna None
print(dicionario.get('cidade'))

# Adicionando novos pares chave-valor
dicionario['profissao'] = 'Engenheiro'
print(dicionario)

# Alterando o valor de uma chave existente
dicionario['idade'] = 31
print(dicionario)

# Removendo um par chave-valor
del dicionario['cidade']
print(dicionario)

# Organizando o dicionário com o método sorted()
print(sorted(dicionario)) # Retorna uma lista com as chaves ordenadas

# Verificando se uma chave existe no dicionário
print('nome' in dicionario) # Retorna True

#
# Iterando sobre um dicionário usando o método items() para obter as chaves e valores
# #
for chave, valor in dicionario.items():
    print(chave, valor)