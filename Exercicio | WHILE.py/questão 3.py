import os
os.system ("cls || clear")

    # Solicitando dados
numero = int(input("Informe o número que quer multiplicar: "))
fator = int(input("Informe por quanto quer multiplicar: "))

# Definindo valores das váriaveis
cont_multiplicacao = 0

# Condicionais
while True:
    if numero > 100:
        break
    numero *= fator
    cont_multiplicacao += cont_multiplicacao + 1

print(f"O produto final: {numero}")
print(f"Multiplicações {cont_multiplicacao}")