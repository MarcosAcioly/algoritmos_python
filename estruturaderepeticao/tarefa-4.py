# 4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#     e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa em Python
#     que calcule e escreva o número de anos necessários para que a população do país A iguale ou ultrapasse a
#     população do país B, mantidas as taxas de crescimento.


# População inicial dos países
populacao_a = 80000
populacao_b = 200000

# Taxas de crescimento anual
taxa_crescimento_a = 0.03  # 3%
taxa_crescimento_b = 0.015  # 1.5%

# Contador de anos
anos = 0

# Loop para calcular o crescimento populacional até que A >= B
while populacao_a < populacao_b:
    # Atualiza as populações com base nas taxas de crescimento
    populacao_a += populacao_a * taxa_crescimento_a
    # populacao_a = populacao_a + (populacao_a * taxa_crescimento_a)
    populacao_b += populacao_b * taxa_crescimento_b

    # Incrementa o contador de anos
    anos += 1

# Exibe o resultado
print(f"Serão necessários {anos} anos para que a população do país A iguale ou ultrapasse a população do país B.")
print(f"População de A após {anos} anos: {populacao_a:.0f}")
print(f"População de B após {anos} anos: {populacao_b:.0f}")



