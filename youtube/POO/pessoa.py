class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    @property
    def idade(self):
        return self._idade

    @property
    def nome(self):
        return self._nome

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = valor

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor
