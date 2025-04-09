# 8 - Faça um algoritmo que pergunte o preço de três produtos e informa qual produto você deve comprar,
#     sabendo que a decisão é sempre pelo mais barato.

p1 = 0
p2 = 0
p3 = 0

p1 = int(input("Digite o preço do primeiro produto: "))

p2 = int(input("Digite o preço do segundo produto: "))

p3 = int(input("Digite o preço do terceiro produto: "))

# Verifica qual é o menor valor


if p1 == 2 and p1 == p3:
    print(f"Podes comprar qualquer um porque os preços são iguais.")

if p1 < p2 and p1 < p3:
    menor = p1
    print(f"O produto com menor preço custa: ", menor)
elif p2 < p1 and p2 < p3:
    menor = p2
    print(f"O produto com menor preço custa: ", menor)
else:
    menor = p3
    print(f"O produto com menor preço custa: ", menor)















# if (p1 == p2) and (p1 == p3):
#    (f"Os números são iguais: ")

# elif (p1 <> p2) and (p1 > p3):
#    print(p1, "O maior é o número")

# elif (p2 > p3):
#    print(p2, "O maior é o número")

# else:
#    print(3, "O maior é o número")

#   # Exibe o resultado
#    print(f"O maior número é: {maior}")
#   print(f"O menor número é: {menor}")