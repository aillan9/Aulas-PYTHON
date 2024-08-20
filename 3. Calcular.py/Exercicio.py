import os 
os.system("cls || clear") #limpa o terminal

# Solicitando dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))

# Definindo media-
media = (nota_1 + nota_2 + nota_3) /3


# Exibindo dados

print(f"Nome:  : {nome}")
print(f"Idade:  : {idade}")
print(f"Média: : {media}")


# Condicionais

if media >= 7:
    print("O aluno está aprovado.")

else: 
    print("O aluno está reprovado.")