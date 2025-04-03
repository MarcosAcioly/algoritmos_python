# Solicitando o nome do usuário
print()
nome = input("Olá! Boa noite! Qual é o seu nome?: ")

print()  # Linha em branco para melhorar a legibilidade

# Solicitando o salário por hora com validação
while True:
    try:
        sh = float(input("Quanto você ganha por hora?: "))
        break
    except ValueError:
        print("Por favor, insira um número válido.")

print()  # Linha em branco para melhorar a legibilidade

# Solicitando as horas trabalhadas por mês com validação
while True:
    try:
        ht = float(input("Quantas horas você trabalha por mês?: "))
        break
    except ValueError:
        print("Por favor, insira um número válido.")

print()  # Linha em branco para melhorar a legibilidade

# Calculando o salário
resultado = sh * ht

# Exibindo o resultado formatado
print(f"Obrigado pelas informações, {nome}! O valor do seu salário é: R${resultado:.2f}")

















from gettext import lngettext

# Recebendo entrada do usuário
print()
nome = (input("Olá! Boa noite! Qual é o seu nome?: "))
print()

nome = {}
sh = float(input("Olá! Boa noite! Quanto você ganha por hora?: "))
print()
ht = float(input("Ok. Quantas horas você trabalha por mês?: "))

print()

resultado = (sh * ht)

print()

# Exibindo o resultado
print(f"Obrigado pelas informações, {nome}! O valor do seu salário é: R${resultado:.2f}")


print()
