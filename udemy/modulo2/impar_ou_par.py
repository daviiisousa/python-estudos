def imparOuPar(numero):
    if numero % 2 == 0:
        return "Par"
    
    return "Ímpar"

def multiplicar(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar(2, 3, 4))