import os
os.system ("cls || clear")

# Definindo valores as variaveis
soma = 0
media = 0
notas = 0

# Solicitando dados
for i in range (3):
    notas = float(input("Digite {i+1}º nota: "))
    soma = soma + notas
media = soma / 3

if notas >= 7:
    print("Você foi aprovado.")
elif notas <4:      # else if
    print:("Você foi reprovado".)
else:
    print("Você está de recuperação")
