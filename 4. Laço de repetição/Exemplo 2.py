import os
os.system ("cls || clear")

# Solicitando dados.
numero = int(input("Digite um número para tabuada: "))

print(f"\n Tabuada de multiplicação do número: {numero}")
for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")