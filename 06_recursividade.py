"""
    O fatorial de um número inteiro n > 1 pode ser definido, RECURSIVAMENTE, como n! = n * (n - 1)!
    Por definição, 1! = 1

    Dessa forma:
    5! = 5 * (5 - 1)! => 5! = 5 * 4!
    4! = 4 * (4 - 1)! => 4! = 4 * 2!
    3! = 3 * (3 - 1)! => 3! = 3 * 2!
    2! = 2 * (2 - 1)! => 2! = 2 * 1! 
    1! = 1 (por definição)

    Dessa forma, para calcular 5!, é necessário calcular antes 4!.
    Para Calcular 4!, é necessário calcular antes 3!, e assim por diante, até chegar em 1! = 1.

"""

# Versão iterativa (não recursiva) para o cálculo do fatorial

def fatorial_iter(n):
    resultado = 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado

#n = int(input("\nDigite um número para ver seu fatorial: "))

#print(f"\nFatorial de {n}: {fatorial_iter(n)}\n" )

# Função recursiva para o cálculo do fatorial 

def fatorial_rec(n):
    if n < 0:
        resultado = None
    elif n in [0, 1]:
        resultado =1
    else:
        resultado = n * fatorial_rec(n - 1) # n! = n * (n - 1)!
    return resultado

num = 0

print(f"\nFatorial iterativo de {num}: {fatorial_iter(num)}")
print(f"\nFatorial recursivo de {num}: {fatorial_rec(num)}")
