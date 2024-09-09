import os
os.system ("cls || clear")

# Declarando valor as váriaveis
soma = 0
contador = 0

while True:
    notas = float(input("Informe uma nota: "))
    contador += 1
    soma += notas

    # Definindo valor das variáveis
    resposta = input("Você deseja digitar mais uma nota? (S) PARA sim e (N) PARA não: ")

    if resposta == "N" or "n":
        break

# Declarando média
media = soma /contador

print(f"Media: {media}")
