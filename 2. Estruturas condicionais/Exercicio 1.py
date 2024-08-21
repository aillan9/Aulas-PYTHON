import os

os.system("cls || clear")

# Solicitando dados
login = input("Digite o seu login: ")
senha = input("Digite a sua senha: ")

# Definindo login e senha corretos
login_correto = ("aillanlima")
senha_correta = ("aillanlindo")

# Definindo condicionais
if login == login_correto and senha == senha_correta:
    print("Login e senha estão corretos, seja bem vindo!")

else:
    print("O seu login ou a sua senha estão inválidos")
    
