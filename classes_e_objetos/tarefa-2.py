# 2 - Classe Auadrado: Crie uma classe que modele um quadrado:

# A - Atributos: Tamanho do lado

# B - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área.


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.__tamanho_do_lado = tamanho_do_lado

    def mudar_tamanho_do_lado(self, novo_tamanho_do_lado):
        self.__tamanho_do_lado = novo_tamanho_do_lado

    def exibir_tamanho_do_lado(self):
        return self.__tamanho_do_lado

    def exibir_area(self):
        return self.__tamanho_do_lado * self.__tamanho_do_lado


cubo = Quadrado(9)
print(cubo.exibir_area())

cubo.mudar_tamanho_do_lado(6)
print(cubo.exibir_area())