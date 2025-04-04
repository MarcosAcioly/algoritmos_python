#  9 – Faça um algoritmo que pela a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32)/9)

# Solicitando ao usuário a temperatura em graus Fahrenheit
print()
print()
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
print()

# Convertendo para graus Celsius usando a fórmula
celsius = (5 / 9) * (fahrenheit - 32)
print()

# Exibindo o resultado formatado
print(f"A temperatura em graus Celsius é: {celsius:.2f}")

