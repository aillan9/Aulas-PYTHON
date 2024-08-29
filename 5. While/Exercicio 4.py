import os
os.system ("cls || clear")

# Definindo login e senhas corretos
login_c = "aillan"
senha_c = "123"

# Definindo o max de tentativas
max_tentativas = (3)
tentativas = 0

# WHILE

while tentativas < max_tentativas:
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

    if login == login_c and senha == senha_c:
        print("Seja bem vindo!")
        break
    else:
        tentativas += 1
        if tentativas < max_tentativas:
            print(f"Login ou senha incorretos, você tem {max_tentativas - tentativas} chances")
        else:
            print("Número de tentativas esgotado.")


