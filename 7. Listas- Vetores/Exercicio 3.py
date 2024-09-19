import os 

os.system ("cls || clear")

# Entrada
QUANTIDADE_DE_NOTAS = 4
lista_notas = []

for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input("Informe uma nota: "))
    lista_notas.append(nota)

# Processamento.
soma= sum(lista_notas)
media = soma / QUANTIDADE_DE_NOTAS

if media >= 7:
    situacao = "Aprovado."
elif media >= 5 and media <= 6.9:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Saída.
print("\n ===== Exibindo resultados =====")
for i, nota in enumerate (lista_notas):
    print(f"{i+1}° Nota: {nota}")
    
    
print(f"Média: {media}")
print(f"Resultado: {situacao}")