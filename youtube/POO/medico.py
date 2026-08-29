from pessoa import Pessoa


class Medico(Pessoa):
    def __init__(self, nome, idade, especialidade):
        super().__init__(nome, idade)
        self.especialidade = especialidade

    def apresentar(self):
        super().apresentar()
        print(f"Eu sou um médico especializado em {self.especialidade}.")
