# Faça um programa para imprimir:
#
#       1
#       1   2
#       1   2   3
#       ............
#       1   2   3 ... n
#
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
#
#

def imprimir_sequencia(n):
    """
    Função que imprime a sequência até a n-ésima linha.

    Parâmetros:
    n (int): Número de linhas da sequência.
    """
    for i in range(1, n + 1):
        # Cria uma lista com números de 1 até i e junta os elementos com espaços
        linha = "   ".join()
        print(linha)


# Solicita ao usuário o valor de n
try:
    n = int(input("Digite o valor de n: "))
    if n > 0:
        imprimir_sequencia(n)
    else:
        print("Por favor, insira um número inteiro positivo.")
except ValueError:
    print("Entrada inválida. Insira um número inteiro.")
