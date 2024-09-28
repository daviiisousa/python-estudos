def exibir_lista_de_frutas_e_qtd( qtd, lista ):
    for i in range(len(lista)):
        print(f"{qtd[i]} {lista[i]} em estoque  ")

def adicionar_nova_fruta(lista, qtd):
    nova_fruta = input("adicione uma nova fruta: ")
    lista.append(nova_fruta)

    nova_qtd = input("qual a quantidade? ")
    qtd.append(nova_qtd)

def adicionar_mais_uma_fruta(lista, qtd):
    nova_fruta = input("deseja adicionar mais uma fruta (sim/nao) ? ")
    if nova_fruta == "sim":
        nova_fruta = input("qual a fruta ? ")
        lista.append(nova_fruta)
    elif nova_fruta == "nao":
        return
    else:
        print("pfv tente novamente e digite uma opçao valida")

    nova_qtd = input("qual a quantidade? ")
    qtd.append(nova_qtd)

lista_de_frutas = ["banana", "maça", "caju"]
lista_qtd = [10, 20, 30]

print("Lista de Frutas e quantidade: ")
exibir_lista_de_frutas_e_qtd(lista_qtd, lista_de_frutas)

adicionar_nova_fruta(lista_de_frutas, lista_qtd)

adicionar_mais_uma_fruta(lista_de_frutas, lista_qtd)
print("Nova Lista: ")
print(f"{lista_qtd[0]} {lista_de_frutas[0]} em estoque")
print(f"{lista_qtd[1]} {lista_de_frutas[1]} em estoque")
print(f"{lista_qtd[2]} {lista_de_frutas[2]} em estoque")
print(f"{lista_qtd[3]} {lista_de_frutas[3]} em estoque")
print(f"{lista_qtd[4]} {lista_de_frutas[4]} em estoque")
