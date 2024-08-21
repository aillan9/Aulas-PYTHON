import os
os.system("cls || clear")

# Organizando dias
print("""
1- Domingo
2- Segunda
3- Terça
4- Quarta
5- Quinta      
6- Sexta      
7- Sabado      
""")
print("______________________________")

opcao = int(input("Digite um número referente ao dia da semana: "))

match(opcao):

    case 1:
        print("O dia da semana escolhido foi domingo, que é no final de semana.")

    case 2:
        print("O dia da semana escolhido foi segunda, que é um dia útil.")

    case 3:
        print("O dia da semana escolhido foi terça, que é um dia útil.")

    case 4:
        print("O dia da semana escolhido foi quarta, que é um dia útil.")

    case 5:
        print("O dia da semana escolhido foi quinta, que é um dia útil.")

    case 6:
        print("O dia da semana escolhido foi sexta, que é um dia útil.")

    case 7:
        print("O dia da semana escolhido foi sabádo, que é no final de semana.")

    case _:
        print("Inválido")





