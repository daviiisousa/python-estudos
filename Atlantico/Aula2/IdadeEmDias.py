valor = int(input())

anos = valor // 365

dias_totais = valor % 365

meses = dias_totais // 30

dias = dias_totais % 30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
