import os
os.system("cls || clear")

# Solicitando dados
soma = 0

for i in range(3):
    nota = int(input("Digite uma nota: "))
    soma = soma + nota
print(f"Soma: {soma}")