"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""
valor = int(input())  # Tempo total em segundos

hora = valor // 3600  # Calcula as horas inteiras
minuto = (valor % 3600) // 60  # Calcula os minutos restantes após contabilizar as horas
segundo = valor % 60  # Calcula os segundos restantes

print(f"{hora}:{minuto}:{segundo}")  # Saída formatada em horas:minutos:segundos
