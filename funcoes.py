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