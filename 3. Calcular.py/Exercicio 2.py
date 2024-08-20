import os
os.system("cls || clear") 

# Solicitando dados

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calculando
media = (numero1 + numero2) /2
soma = numero1 + numero2
produto = numero1 * numero2

# Exibindo dados

print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

# Definindo condicionais

if numero1 > numero2:
    print("O primeiro número é o maior valor")

else:
    print("O segundo número é o maior valor")


