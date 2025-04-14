
# Faça um algoritmo para imprimir:
#
#       1
#       2   2
#       3   3   3
#       .............
#       n   n   n   n   n ... n
#
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


def imprimir_padrao(n):
    """
    Função que imprime o padrão até a n-ésima linha.

    Parâmetros:
    n (int): Número de linhas do padrão.
    """
    for i in range(1, n + 1):
        # Cria uma lista com 'i' repetido 'i' vezes e junta os elementos com espaços
        linha = "   ".join([str(i)] * i)
        print(linha)


# Solicita ao usuário o valor de n
try:
    n = int(input("Digite o valor de n: "))
    if n > 0:
        imprimir_padrao(n)
    else:
        print("Por favor, insira um número inteiro positivo.")
except ValueError:
    print("Entrada inválida. Insira um número inteiro.")