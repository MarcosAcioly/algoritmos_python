# 7 - Faça um algoritmo que leia três números e mostre o maior e o menor deles.

# Solicita três números ao usuário
print()
n1 = float(input("Digite o primeiro número: "))
print()
n2 = float(input("Digite o segundo número: "))
print()
n3 = float(input("Digite o terceiro número: "))

print()

# Encontra o maior número
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

# Encontra o menor número
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

# Exibe o resultado
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")