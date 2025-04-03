

from gettext import lngettext

# Recebendo entrada do usuário
print()
n1 = float(input("Por favor, digite o primeiro número: "))

print()

n2 = float(input("Por favor, digite o segundo número: "))

print()

# Somando os números
resultado = n1 + n2

print()

# Exibindo o resultado
print("A soma do número", n1, " + ", n2, "é: ", resultado)

print()






# Função para somar dois números
def somar(a, b):
    return a + b

try:
    # Recebendo entrada do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Chamando a função e exibindo o resultado
    resultado = somar(num1, num2)
    print("A soma é:", resultado)

except ValueError:
    print("Erro: Por favor, insira números válidos.")


    # Função para somar dois números
    def somar(a, b):
        return a + b


    try:
        # Recebendo entrada do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Chamando a função e exibindo o resultado
        resultado = somar(num1, num2)
        print("A soma é:", resultado)

    except ValueError:
        print("Erro: Por favor, insira números válidos.")



