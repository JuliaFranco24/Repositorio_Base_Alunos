#Exercício 1: Validação de Entrada Inteira
# Escreva um programa que solicite um número inteiro ao usuário. Use try-except para tratar entradas não numéricas e valores não inteiros.
#  Se ocorrer um erro, peça a entrada novamente até que seja válida.

num1=input("Digite um número:")


try:
    num1=int(num1)
    

    print(f"O número é: {num1}")
except:
    print("Digite um número correto!")