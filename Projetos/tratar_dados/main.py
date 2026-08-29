import os

from tratar_dados import TratarCSV


def main():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    arquivo_entrada = os.path.join(diretorio_atual, "dados_clientes_brutos.csv")
    arquivo_saida = os.path.join(diretorio_atual, "dados_clientes_tratados.csv")

    tratar_csv = TratarCSV(arquivo_entrada, arquivo_saida)
    tratar_csv.processar()
    tratar_csv.salvar()


if __name__ == "__main__":
    main()
