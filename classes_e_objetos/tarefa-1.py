# Tarefa - 1

# 1 – Classe Bola: Crie uma classe que modele uma bola:

# A - Atributos: Cor, ciscunferencia, material
# B – Metodos: trocaCor e mostraCor


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def trocaCor(self):
        self.__cor = cor

    def mostraCor(self):
        return self.__cor


bola_football = Bola("branca com gomos azuis", 32, "couro")

print(bola_football.mostraCor())