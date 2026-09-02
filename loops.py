#
# Estruturas de repetição
# ============================================================== #

abcdario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '...']
inic = 0
fim = 0
passo = 0
rang = []

# 
# Laço FOR
# ==============================================================#

# O laço for em python serve única e exclusivamente para iterar sobre uma coleção de dados.
# Utiliza a palavra in para fazer a passagem dos valores.
# #
print ("As primeiras letras do alfabeto são: ")
for abc in abcdario:
    print (abc, end= ", ")


# A função range() do python serve para criar uma sequência númerica (lista) iteravel.
# Ela possui os seguintes parâmetros: range(início?, fim, passo?)
#   início -> é o ponto de partida da sequência (opcional), caso no seja informado, o padrão será 0
#   Fim -> o limimite (o qual a sequência nunca alcança)
#   passo -> Razão da sequência (opcional), caso no seja informado, o padrão será 1
# # 
print ("\n\nCrie sua sequência!")

inic = int(input("Digite o número inícial da sequência: "))
fim = int(input("Digite o número limite da sequência: "))
passo = int(input("Digite o passo da sequência: "))

rang = range(inic, fim, passo)

for i in rang:
    print (i, end=", ")

# continue e break
# As palavras reservadas continue e break são utilizadas para controlar o fluxo de execução de um laço.
# A palavra continue faz com que o laço ignore a iteração atual e passe para a próxima iteração.
# A palavra break faz com que o laço seja interrompido, e a execução do programa continue a partir da linha seguinte ao laço.
countComp = 0
countPri = 0

for i in range(100):
    for a in range(i):
        if a == 0:
            a = 1
        
        if i%a != i & i%a != 1:
            i=0
            countComp += 1
            break
    if i == 0:
        continue
    else:
        countPri += 1

print ("\nDe 0 à 100 existem", countComp, "números compostos e", countPri, "números primos!")

# 
# Laço WHILE
# ==============================================================#
# O laço while em python executa um bloco de código enquanto uma condição for verdadeira.

count = 0
while count < 10:
    print (count, end=", ")
    count += 1

# 
# função pass
# A função pass não faz nada, mas é utilizada quando é necessário 
#   sintaticamente ter um bloco de código, mas não deseja executar nenhum comando.
# #

# while True:
#     pass


#
# Clausula else em laços
# ==============================================================#
# A cláusula else pode ser utilizada em laços for e while.
# O bloco de código dentro da cláusula else será executado quando a condição do 
#   laço não for mais verdadeira. Esse bloco de código não será executado caso o 
#   laço seja interrompido por um break.
# #

for i in range(5):
    print(i, end=", ")
else:
    print("Fim do laço!")

while count < 5:
    print(count, end=", ")
    count += 1
else:
    print("Fim do laço!")