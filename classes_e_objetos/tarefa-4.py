# TAREFA 4

# CLASSE PESSOA:  Crie uma classe que modele uma pessoa:

#   A - Atributos: nome, idade, peso e altiura

#   B - Métodos: Envelhecer, engordar, emagrecer, crescer.
#   Obs.: Por padrão, a cada ano que nossa pessoal envelhece,
#   sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        """
        Construtor da classe Pessoa.

        :param nome: Nome da pessoa (str).
        :param idade: Idade da pessoa em anos (int).
        :param peso: Peso da pessoa em kg (float).
        :param altura: Altura da pessoa em metros (float).
        """
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos: int = 1):
        """
        Método para envelhecer a pessoa. A cada ano, se a idade for menor que 21,
        a pessoa cresce 0,5 cm.

        :param anos: Quantidade de anos para envelhecer (padrão: 1).
        """
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.crescer(0.5)

    def engordar(self, quilos: float):
        """
        Método para aumentar o peso da pessoa.

        :param quilos: Quantidade de peso a ser adicionada (em kg).
        """
        self.peso += quilos

    def emagrecer(self, quilos: float):
        """
        Método para reduzir o peso da pessoa.

        :param quilos: Quantidade de peso a ser removida (em kg).
        """
        self.peso -= quilos
        if self.peso < 0:  # Garantindo que o peso não fique negativo.
            self.peso = 0

    def crescer(self, centimetros: float):
        """
        Método para aumentar a altura da pessoa.

        :param centimetros: Quantidade de altura a ser adicionada (em cm).
        """
        self.altura += centimetros / 100  # Convertendo cm para metros.

    def __str__(self):
        """
        Representação textual da pessoa.
        """
        return (f"Pessoa(nome={self.nome}, idade={self.idade} anos, "
                f"peso={self.peso:.2f} kg, altura={self.altura:.2f} m)")

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Pessoa
    pessoa = Pessoa(nome="João", idade=19, peso=63.5, altura=1.65)
    print(pessoa)

    # Envelhecendo a pessoa por 3 anos
    pessoa.envelhecer(3)
    print("\nApós envelhecer 3 anos:")
    print(pessoa)

    # Engordando a pessoa
    pessoa.engordar(5)
    print("\nApós engordar 5 kg:")
    print(pessoa)

    # Emagrecendo a pessoa
    pessoa.emagrecer(3)
    print("\nApós emagrecer 3 kg:")
    print(pessoa)

    # Crescendo manualmente
    pessoa.crescer(4)
    print("\nApós crescer 4 cm:")
    print(pessoa)


