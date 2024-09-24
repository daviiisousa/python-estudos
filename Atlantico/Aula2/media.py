"""Nota1 = float(input("digite sua nota "))
Nota2 = float(input("Digite sua nota "))
Nota3 = float(input("digite sua nota "))

media = (Nota1 + Nota2 + Nota3) / 3
print("Sua media é ", media)"""

media = 0

for i in range(1, 4):
    nota = float(input(f"digite sua nota {i} "))

    media += nota

print(media // 3)