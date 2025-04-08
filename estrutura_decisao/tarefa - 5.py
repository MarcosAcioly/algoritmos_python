# 5 - Faça um algoritmo para a leitura de duas notas parciais de um alno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado". se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "aprovado com Distincção", se a média for igual a dez.

# Leitura das notas parciais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação da média e exibição da mensagem correspondente
if media == 10:
    print(f"Média: {media:.2f} - Aprovado com Distinção")
elif media >= 7:
    print(f"Média: {media:.2f} - Aprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")




















