import os
os.system ("cls || clear")

# Organizando cardápio
print(""" 
        CARDÁPIO DO RESTAURANTE
   Código  |    Prato     | Valor
    
      1    |  Picanha     | R$ 25,00
      2    |  Lasanha     | R$ 20,00
      3    |  Strogonoff  | R$ 18,00
      4    |Bife acebolado| R$ 15,00
      5    | Pão com ovo  | R$ 5,00
""")
print("______________________________")

opcao = int(input("Digite o código do seu pedido: "))

match (opcao):
    case 1:
        print("Seu pedido foi um prato de Picanha!")
    case 2: 
        print("Seu pedido foi um prato de Lasanha!")
    case 3:
        print("Seu pedido foi um prato de Strogonoff")
    case 4:
        print("Seu pedido foi um prato de Bife acebolado")       
    case 5: 
        print("Seu pedido foi um Pão com ovo")
    case _:
        print("Opção inválida")


 