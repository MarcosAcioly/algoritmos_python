# Loop para continuar pedindo a nota até que seja válida
while True:
    # Solicitar ao usuário que insira uma nota
    nota = float(input("Digite a nota: "))

    # Verificar se a nota está no intervalo válido
    if 0 <= nota <= 10:
        print("Nota OK")
        break  # Encerra o loop quando a nota for válida
    else:
        print("Nota inválida")  # Exibe mensagem de erro e continua o loop