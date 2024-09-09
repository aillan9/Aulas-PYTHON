import os
os.system ("cls || clear")
# Solicita o número inicial e o fator ao usuário

numero_inicial = float(input("Digite o número inicial: "))
fator = float(input("Digite o fator de multiplicação: "))

multiplicacoes = 0

# Loop que continua até que o produto exceda 100
while True:
    if numero_inicial > 100:
        break
    numero_inicial *= fator
    multiplicacoes += 1

# Exibe o produto final e o número de multiplicações realizadas
print(f"O produto final é: {numero_inicial}")
print(f"Número de multiplicações realizadas: {multiplicacoes}")
