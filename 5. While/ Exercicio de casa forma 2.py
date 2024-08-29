import os
os.system ("cls || clear")

# Definindo valor da váriavel soma
soma = 0

# Laços, condicionais, while e etc...
for i in range (3):
    while True:
        notas = float(input(f"Informe sua {i+1}º nota: "))

        if notas >= 0 and notas <= 10:
            break
        else:
            print("As notas devem ser menoriguais a 10 ou maioriguais a 0")

# Definindo média
soma += notas + notas + notas
media = soma /3

# Definindo aprovação, recuperação e etc..
if media >= 7:
    print("Você foi aprovado!")
elif media >= 5 and media < 7:
    print("Você está de recuperação!")
else:
    print("Você foi reprovado!")


print(f"Média: {media}")




