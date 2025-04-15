#   4 - Faça um programa, com uma função que necessite de um argumento.
#   A função retorna o valor de caractere 'P', se seu argumento for
#   positivo,  e 'N', se seu argumento for zero ou negativo.
#
#
def verifica_numero(numero):
    """
    Função que verifica se um número é positivo, zero ou negativo.

    Parâmetros:
    numero (int ou float): O número a ser verificado.

    Retorna:
    str: 'P' se o número for positivo, 'N' se o número for zero ou negativo.
    """
    if numero > 0:
        return 'P'
    else:
        return 'N'


# Solicita ao usuário um número
try:
    num = float(input("Digite um número: "))

    # Chama a função e exibe o resultado
    resultado = verifica_numero(num)
    print(f"O resultado é: {resultado}")
except ValueError:
    print("Entrada inválida. Insira um número válido.")