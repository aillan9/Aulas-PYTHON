import os
os.system ("cls || clear")

# Solicitando dados do usuário
altura = float(input("Digite sua altura: "))

sexo = input("Digite seu sexo (M ou F): ")

# Verificando 

match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _: 
        print("Opção inválida.")

print(f"Peso ideal; {peso_ideal}")