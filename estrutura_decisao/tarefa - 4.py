# 4 - Faça um algoritmo no Python que verifique se uma letra digitada é vogal ou consoante.

# Solicita ao usuário que digite uma letra
while True:
    letra = input("Digite uma letra: ").lower()  # Converte a entrada para minúscula

# Verifica se a entrada é uma letra do alfabeto
    if len(letra) == 1 and letra.isalpha():  # Garante que seja apenas uma letra
        if letra in "aeiou":  # Verifica se é uma vogal
            print(f"A letra '{letra}' é uma vogal.")
            break
        else:  # Caso contrário, é uma consoante
            print(f"A letra '{letra}' é uma consoante.")
            break
    else:
        print("Entrada inválida. Digite apenas uma letra do alfabeto.")

