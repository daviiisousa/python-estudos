import csv
from datetime import datetime
import re


class TratarCSV:
    def __init__(self, arquivo_entrada, arquivo_saida):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo_saida = arquivo_saida
        self.linhas_tratadas = []

    def processar(self):
        with open(self.arquivo_entrada, "r", encoding="utf-8-sig") as file:
            leitor = csv.DictReader(file)
            ids_vistos = set()

            for linha in leitor:
                id_cliente = linha["id_cliente"].strip()

                if id_cliente in ids_vistos:
                    continue
                ids_vistos.add(id_cliente)

                nome = linha["nome_cliente"].strip().title()
                if not nome or nome == "N/A":
                    continue

                categoria = linha["categoria_produto"].strip().capitalize()
                if not categoria or categoria == "N/A":
                    continue

                valor_limpo = (
                    linha["valor_compra"]
                    .replace("R$", "")
                    .replace(" ", "")
                    .replace(".", "")
                    .replace(",", ".")
                )
                if not valor_limpo or valor_limpo == "N/A":
                    continue

                try:
                    valor = float(valor_limpo)
                except ValueError:
                    valor = 0.0

                idade = linha["idade"].strip()
                if not idade or idade == "N/A":
                    continue
                try:
                    idade = int(idade)
                    if idade < 0:
                        continue
                except ValueError:
                    continue

                email = linha["email"].strip().lower()
                if not email or email == "N/A":
                    continue

                regex_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
                if not re.match(regex_email, email):
                    continue

                data_cadastro = linha["data_cadastro"].strip()
                if not data_cadastro or data_cadastro == "N/A":
                    continue

                data_formatada = None

                formatos_possiveis = [
                    "%Y-%m-%d",
                    "%d/%m/%Y",
                    "%d-%m-%Y",
                    "%Y.%m.%d",
                    "%Y/%m/%d",
                ]
                for fmt in formatos_possiveis:
                    try:
                        data_formatada = datetime.strptime(data_cadastro, fmt)
                        break
                    except ValueError:
                        continue

                if data_formatada is None:
                    continue

                linha_tratada = {
                    "id_cliente": id_cliente,
                    "nome_cliente": nome,
                    "data_cadastro": data_formatada.strftime("%Y-%m-%d"),
                    "idade": idade,
                    "valor_compra": f"{valor:.2f}",
                    "categoria_produto": categoria,
                    "email": email,
                }

                self.linhas_tratadas.append(linha_tratada)

    def salvar(self):
        if not self.linhas_tratadas:
            print("Nenhum dado disponível para salvar.")
            return

        colunas = self.linhas_tratadas[0].keys()

        with open(self.arquivo_saida, "w", encoding="utf8", newline="") as file:
            escritor = csv.DictWriter(file, fieldnames=colunas)
            escritor.writeheader()
            escritor.writerows(self.linhas_tratadas)
        print(f"Dados salvos em {self.arquivo_saida}")
