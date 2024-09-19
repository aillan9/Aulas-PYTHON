import os
os.system ("cls || clear")

vetor_valores = []

for i in range (5):
    valor = float(input(f"Informe {i+1}º valor: "))
    if valor < 0:
        valor = 0
    vetor_valores.append(valor)

print("\n === Exibindo dados ===")
for cada_numero in vetor_valores:
    print(cada_numero)