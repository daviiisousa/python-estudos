def exibir_lista_de_frutas_e_qtd( qtd, lista ):
    for i in qtd:
        print(f"{i} quantidade em estoque ")

    for i in lista:
        print(f"{i} ")
    
def adicionar_nova_fruta(lista, qtd):
    nova_fruta = input("adicione uma nova fruta: ")
    lista.append(nova_fruta)

    nova_qtd = input("qual a quantidade? ")
    qtd.append(nova_qtd)

lista_de_frutas = ["banana", "maça", "caju"]
lista_qtd = [10, 20, 30]

print("Lista de Frutas e quantidade: ")
exibir_lista_de_frutas_e_qtd(lista_qtd, lista_de_frutas)


print()
adicionar_nova_fruta(lista_de_frutas, lista_qtd)
print("nova lista de fruta e quantidade: ", lista_de_frutas, lista_qtd)