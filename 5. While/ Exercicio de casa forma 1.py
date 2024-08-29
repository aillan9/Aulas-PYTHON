import os
os.system ("cls || clear")

# Definindo valores à variáveis
soma = 0
nota1 = 0
nota2 = 0
nota3 = 0

while True:
            # Validação da primeira nota
            nota1 = float(input(f"Infome a primeira nota nota: "))
            if nota1 >= 0 and nota1 <= 10:
                  break
            else:
                  print("As notas precisam ser maior ou iguais a 0 ou menor ou iguais a 10")

            # Validação da segunda nota
while True:
            nota2 = float(input(f"Infome a seguda nota nota: "))
            if nota2 >= 0 and nota2 <= 10:
                  break
            else:
                  print("As notas precisam ser maior ou iguais a 0 ou menor ou iguais a 10")

            # Validação da terciera nota
while True:
            nota3 = float(input(f"Infome a terceira nota nota: "))
            if nota3 >= 0 and nota3 <= 10:
                  break
            else:
                  print("As notas precisam ser maior ou iguais a 0 ou menor ou iguais a 10")

# Definindo média
soma += nota1 + nota2 + nota3
media = soma /3

# Definindo aprovação, recuperação e etc...
if media >= 7:
      print("Você está aprovado!")
elif media >= 5 and media <= 6.9:
    print("Você está de recuperação")
else:
      print("Você está reprovado!")

print(f"Média: {media:.2f}")