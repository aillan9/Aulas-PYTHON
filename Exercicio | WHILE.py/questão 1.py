import os
os.system ("cls || clear")

# Criando váriavel de contagem de número negativo
cont_negativo = 0

while True:
    num_negativo = int(input("Informe um número negativo (Digite um número positivo ou 0 para sair): "))

    if num_negativo > 0:
        break
    
    cont_negativo += 1
    
print(f"Quantidade de números negativos: {cont_negativo}")

