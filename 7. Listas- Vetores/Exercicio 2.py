import os 

os.system ("cls || clear")

def calcular_media(n1, n2, n3):
    return (nota1 + nota2 + nota3) /3

# Entrada
QUANTIDADE_DE_NOTAS = 3
lista_de_notas = []

# Processamento
for i in range (QUANTIDADE_DE_NOTAS):
    nota = float(input(f"Informe a {i+1}º nota: "))

media = calcular_media(n1, n2, n3)

print(f"Média: {calcular_media}:.2f")

