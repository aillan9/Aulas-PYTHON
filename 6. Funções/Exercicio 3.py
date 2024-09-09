"""
Escreva um programa que solicite ao utilizador o fornecimento do seu peso em kg e de sua altura em M
e a partir deles calcule o índice de massa corpórea

"""
def calcular_imc(peso, altura):
    resultado = peso / (altura * altura)

def classificar_imc (imc):
   if imc <18.5:
     return"Você está abaixo do peso! Consulte um nutricionista para orientação" 
   elif imc >= 18.5 and imc <= 24.9:
      return"Você está no peso normal, mantenha hábitos saudáveis!"
   elif imc >= 25 and imc <= 29.9:
      return"Sobrepeso, Considere uma dieta balanceada e atividade física"
   elif imc >= 30 and imc <= 34.9:
      return"Você está obeso no grau 1, procure orientação de um profissional de saúde"
   elif imc >= 35 and imc <= 39.9:
      return"Você está obeso no grau 2, Consulte um médico para avaliação e orientação"
   elif imc >= 40
      return"Você está obeso no grau 3, busque assistência médica imediatamente"

#Entrada 
peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))


#Processamento
imc = calcular_imc(imc)
classificar = classificar_imc(imc)
