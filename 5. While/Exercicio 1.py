import os
os.system ("cls || clear")


# Solicitando dados
nota = float(input("Informe sua nota: "))

# Calculando
while nota < 0 or nota > 10:
    print("\nA nota deve ser maior ou igual a 10 e menor ou igual a 0") 
    nota = float(input("Informe sua nota: "))

print("Nota: {nota}")