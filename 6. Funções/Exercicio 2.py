"""
Escreva um programa que permita ler 2 notas de um aluno e:

Informe por meio do DEF a média;

Informe por meio de uma função se a média for maior ou igual a 7, o aluno estará aprovado, caso contrário, estará reprovado.

"""

import os
os.system ("cls || clear")

def calcular_media(nota1,nota2):
    return (nota1 + nota2) /2

def verificar_aprovacao(media):
    if media >= 7:
        return "O aluno está aprovado!"
    else:
        return "O aluno está reprovado!"

# Entrada
nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))

# Processamento
media = calcular_media(nota1,nota2)
resultado = verificar_aprovacao(media)  

# Saída
print(f"Média {media:.2f}")
print(f"O aluno está {resultado}")
