# 3 - Faça um programa que leia e valide as seguintes informações:

# A - Nome: maior que 3 caracteres;
# B - Idade: entre 0 e 150 caracteres;
# C - Salário: maior que zero;
# D - Sexo: 'F' ou 'M';
# E - Estado Civil: 'S', 'C', 'D', 'V';


# Programa principal

print("Por favor, insira os seguintes dados:")

    # Validar Nome (maior que 3 caracteres)
while True:
    nome = input("Nome: ")
    if len(nome) > 3:
        break
    else:
        print("Erro: O nome deve ter mais de 3 caracteres. Tente novamente.")

    # Validar Idade (entre 0 e 150)
while True:
    try:
        idade = int(input("Idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Erro: A idade deve estar entre 0 e 150 anos. Tente novamente.")
    except ValueError:
            print("Erro: Por favor, insira um número inteiro válido para a idade.")

    # Validar Salário (maior que zero)
    while True:
        try:
            salario = float(input("Salário: "))
            if salario > 0:
                break
            else:
                print("Erro: O salário deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido para o salário.")

    # Validar Sexo ('f' ou 'm')
    while True:
        sexo = input("Sexo (f/m): ").lower()
        if sexo in ['F', 'M']:
            break
        else:
            print("Erro: O sexo deve ser 'f' (feminino) ou 'm' (masculino). Tente novamente.")

    # Validar Estado Civil ('S', 'C', 'D', 'V')
    while True:
        estado_civil = input("Estado Civil (S/C/D/V): ").lower()
        if estado_civil in ['S', 'C', 'D', 'V']:
            break
        else:
            print("Erro: O estado civil deve ser 'S' (solteiro), 'C' (casado), 'D' (divorciado) ou 'V' (viúvo). Tente novamente.")

    # Exibir os dados validados
print("\nDados válidos inseridos com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

