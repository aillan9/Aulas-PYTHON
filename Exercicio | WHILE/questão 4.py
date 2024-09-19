"""
Crie um programa que ajude um usuário a controlar seus gastos mensais. 
O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. 
O programa deve exibir o total gasto e o valor  excedente.

Dica: Defina um orçamento e use um laço while para somar os gastos diários. Pare quando o total gasto exceder o orçamento.

"""
import os
os.system ("cls || clear")

# Definindo valor as váriaveis
gasto_total = 0

orcamento = float(input("Informe seu orçamento inicial: "))

while gasto_total <= orcamento:

    # Solicitando dados
    gasto_diario = float(input("Informe seu gasto diário: "))
    gasto_total += gasto_diario



    # Organizando condicionais
    if gasto_total > orcamento:
        break

    excedente = orcamento - gasto_total

print(f"Total gasto: {gasto_total}")
print(f"Valor execedente: {excedente}")




        
     