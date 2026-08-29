produtos = [
    {"nome": "Produto 1", "preco": 10.0},
    {"nome": "Produto 2", "preco": 20.0},
    {"nome": "Produto 3", "preco": 30.0},
]

# Criando uma nova lista de produtos com preços atualizados usando list comprehension
novos_produtos = [
    # Mapeamento
    {**produto, "preco": produto["preco"] * 1.1}
    for produto in produtos
    # Filtro so pode if
    if produto["preco"] > 15.0
]

print(novos_produtos)