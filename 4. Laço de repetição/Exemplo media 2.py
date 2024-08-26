import os
os.system ("cls || clear")

# Definindo valores a variáveis
notas = 0
soma = 0
media = 0

# Definindo dados
for i in range(3):
    notas = float(input(f"Digite {i+1}º nota: "))
    soma = soma + notas

media = soma /3

print(f"Média: {media}")

# Organizando condicionais
if media >= 7 :
    print("Aprovado")
else:
    ("Reprovado")
