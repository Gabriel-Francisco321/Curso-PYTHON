#
# Condição IF () 
# 
# #

# Espera receber um número digitado pelo usuário. A função int converte a entrada em um número inteiro.
numero = int(input("Digite um número: "))

# A intrução são aninhadas atravez da indentação. Intruções internas precisam de um recuo maior.  
if (numero > 0):
    print ("O número é positivo!")
elif (numero == 0): # A instrução elif funciona como uma abreviatura do else if tradicional
    print ("O número é zero!")
else:
    print ("O número é negativo!") 
    # A pós o final de um conjunto de intruções, deve ser deixada uma linha em branco 
    #   para o interpretador saber que se fechou o conjunto

#
# "Condição" match
# Funciona como o switch para a maioria das linguagens de programação# 
opcao = int(input("Digite um número: "))

match opcao:
    case 10:
        print("O número digitado é o 10!")
    case 20:
        print("O número digitado é o 20!")
    case _:
        print("O número digitado é diferente de 10 e de 20")

