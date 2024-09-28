def exibir_lista_de_frutas_e_qtd( qtd, lista ):
    for i in range(len(lista)):
        print(f"|{qtd[i]} {lista[i]} em estoque|")

def adicionar_nova_fruta(lista, qtd):
    nova_fruta = input("adicione uma nova fruta: ")
    if nova_fruta == "":
            print("Fruta não informada")
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
        return

    nova_qtd = input("qual a quantidade? ")
    qtd.append(nova_qtd)

def apagar_um_item(lista, qtd):
    deleatr_item = input("deseja apagar uma fruta? (sim/nao) ")
    if deleatr_item == "sim":
        item_a_remover = input("qual fruta? ")
        lista.remove(item_a_remover)
    elif deleatr_item == "nao":
        return
    else:
         print("pfv tente novamente e digite uma opçao valida")
         return

    print(">>>HORTIFRÚTI ATUALIZADO<<<")
    for i in range(len(lista)):
        print(f"|{qtd[i]} {lista[i]} em estoque|")


lista_de_frutas = ["banana", "maça", "caju"]
lista_qtd = [10, 20, 30]

print(">>>HORTIFRÚTI<<<")

exibir_lista_de_frutas_e_qtd(lista_qtd, lista_de_frutas)

adicionar_nova_fruta(lista_de_frutas, lista_qtd)

adicionar_mais_uma_fruta(lista_de_frutas, lista_qtd)

def exibir_lista_de_frutas_e_qtd_atualizada( qtd, lista ):
    for i in range(len(lista)):
        print(f"|{qtd[i]} {lista[i]} em estoque|")

print(">>>HORTIFRÚTI ATUALIZADO<<<")
exibir_lista_de_frutas_e_qtd_atualizada(lista_qtd, lista_de_frutas)

apagar_um_item(lista_de_frutas, lista_qtd)
