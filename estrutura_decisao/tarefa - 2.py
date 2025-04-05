# 2 - Faça um algoritmo que peça um valor e mostre na tela se o valor é positivo ou negativo.

# Solicita um valor ao usuário

print()
valor = float(input("Digite um valor: "))

print()
# Verifica se o valor é positivo, negativo ou zero
if valor > 0:
    print(f"O valor {valor} é positivo.")
elif valor < 0:
    print(f"O valor {valor} é negativo.")
else:
    print("O valor é zero.")