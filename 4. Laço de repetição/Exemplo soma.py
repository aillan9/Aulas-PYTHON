import os
import time

os.system ("cls || clear")

# Solicitando dados do usuário
soma = 0

for i in range(5):
    numero = int(input(f"Digite {i+1}º número: "))
    soma = soma + numero


print(f"Soma: {soma}")