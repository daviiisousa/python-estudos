lista = [
    1, 2.0, True, 'Olá, mundo!', [1, 2, 3], {'chave': 'valor'}, (1, 2), None
]

for item in lista:
    if isinstance(item, bool):
        print(f"{item} é um booleano.")