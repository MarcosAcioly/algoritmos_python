# 3 - Faça um algoritmo que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
#
# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ").upper()  # Converte a entrada para maiúscula

# Verificação da letra digitada
if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")