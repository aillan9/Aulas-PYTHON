"""
Solicite ao usuário seu login e senha.
o programa deve continuar pedindo login e senha até que ambos estejam corretos
"""
import os
os.system ("cls || clear")

# Definindo login e senha corretos
login_c = "aillan123"
senha_c = "1234567"

# Solicitando dados do usuário
while True:
    login = input("Informe seu login de usuário: ")
    senha = input("Informe a sua senha: ")

    if login == login_c and senha == senha_c:
        print("Seja bem vindo!")
    else: 
        print("Login ou senha incorretos")