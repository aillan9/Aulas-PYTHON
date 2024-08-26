import os
os.system ("cls || clear")

# Definindo valores a variáveis
notas = 0
soma = 0
media = 0

# Definindo dados
for i in range(4):
    notas = float(input(f"Digite {i+1}º nota: "))
    soma = soma + notas

media = soma /4

print(f"Média: {media}")
