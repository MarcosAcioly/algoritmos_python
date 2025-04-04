#  7 – Faça um algoritmo que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# Solicitar o comprimento do lado do quadrado ao usuário
print()
lado = float(input("Digite o comprimento do lado do quadrado: "))
print()

# Calcular a área do quadrado usando a fórmula: área = lado²
area = lado ** 2

# Calcular o dobro da área
dobro_area = area * 2

# Exibir os resultados
print(f"A área do quadrado é: {area:.2f}")
print()
print(f"O dobro da área do quadrado é: {dobro_area:.2f}")
print()