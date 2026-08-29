from medico import Medico
from pessoa import Pessoa


def main():
    pessoa1 = Pessoa("Alice", 30)

    pessoa1.idade = 31
    pessoa1.nome = "Alice Smith"

    pessoa1.apresentar()

    medico1 = Medico("Dr. John", 45, "Cardiologia")
    medico1.apresentar()


if __name__ == "__main__":
    main()
