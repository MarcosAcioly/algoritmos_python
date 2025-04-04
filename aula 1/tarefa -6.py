#  6 – Faça um algoritmo que peça o raio de um círculo, calcule e mostre sua área.

# Importar a biblioteca math para usar o valor de pi
import math

print()
# Solicitar o raio ao usuário
raio = float(input("Digite o raio do círculo: "))

print()
# Calcular a área do círculo usando a fórmula: área = π * r²
area = math.pi * (raio ** 2)

print()
# Exibir o resultado
print(f"A área do círculo com raio {raio} é: {area:.5f}")

