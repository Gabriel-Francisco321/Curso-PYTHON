#
# Funções em python
# 
# Uma função em python é criada usando a palavra reservada def
# Por padrão toda a função retorna none
# É possivel atribuir uma função a uma variável
# #

def fib (n):
    """Função que exibe os números da sequência de fibonacci até o valor digitado"""
    a, b = 0, 1
    while a < n:
        print(a, end=", ")
        a, b = b, b+a

n = int(input("Digite um número: "))

fib(n)

# f = fib
# f(n) # Teria o mesmo resultado que na linha anterior 

# Argumentos opcionais
# ================================================================
def calc (n1, n2, op='+'): # O parametro op é opcional, caso não seja informado, o padrão será '+'
    match op:
        case '+':
            return n1 + n2
        case '*':
            return n1 * n2 
        case '-':
            return n1 - n2
        case '/':
            return n1 / n2
        case _:
            return "indefinido!"
        
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
op = str(input("Digite o operador (padrão: +): "))

print (calc(n1, n2, op))

# Nota: argumentos padão/opcionais são avaliados apenad uma vez, no momento da definição da função. Portanto, se o argumento padrão for um objeto alterável (como uma lista), e esse objeto for modificado, o valor padrão será alterado para todas as chamadas seguintes da função. 

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) #resultará em [1]
print(f(2)) #resultará em [1, 2]
print(f(3)) #resultará em [1, 2, 3]

# Tipos de Argumentos
# ================================================================
#existe 4 tipos de argumentos em python:
#   - Obrigatórios: são os argumentos que devem ser passados para a função, caso contrário, 
#   ocorrerá um erro
#   - Opcionais: são os argumentos que possuem um valor padrão, caso não sejam 
#   passados para a função, o valor padrão será utilizado
# ---------- Já antes referidos --------
#   - Posicionais: são os argumentos que são passados para a função na ordem em que foram definidos
#   - Nomeados: são os argumentos que são passados para a função com o nome do parâmetro, permitindo 
#   que sejam passados em qualquer ordem

# Os argumentos posicionais e nomeados podem ser combinados, mas os posicionais devem ser passados antes dos nomeados.
def exemplo_combinado(somente_pos, /, padrão, *, somente_nom):
    print(somente_pos, padrão, somente_nom)

# para utilizar argumentos posicionais, basta colocar uma barra (/) no final da lista de parâmetros da função, indicando que todos os parâmetros antes da barra são posicionais.

# para utilizar argumentos nomeados, basta colocar um asterisco (*) no início da lista de parâmetros da função, indicando que todos os parâmetros depois do asterisco são nomeados.