import os 
os.system("cls || clear")

# Declarando valores das váriaveis
notas = 0
soma = 0
media = 0

for i in range (2):
    while True:
        notas = int(input(f"Informe sua {i+1}º nota: "))
        
        if notas >= 0 and notas <= 10:
            break
        else:
            print("As notas precisam ser maioriguais a 0 ou menoriguais a 10")

soma += notas
media = soma /2

print(f"Média: {media}")
