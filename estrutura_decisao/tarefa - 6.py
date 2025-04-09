n1 = 0
n2 = 0
n3 = 0

n1 = int(input("Digite o primeiro número: "))

n2 = int(input("Digite o segundo número: "))

n3 = int(input('Digite o terceiro número:  '))



# Verifica qual é o maior número ou se são iguais
if (n1 == n2) and (n1 == n3):
    print(f"Os números são iguais: ")

elif (n1 > n2) and (n1 > n3):
    print(n1, "O maior é o número")

elif (n2 > n3):
    print(n2, "O maior é o número")

else:
    print(n3, "O maior é o número")