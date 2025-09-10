#Crie uma função que receba dois números e uma operação (+, -,*, /) e retorne o resultado da operação.
n1=int (input("Digite um número:"))
n2=int (input("Digite outro número:"))
option=input("multiplicar/somar/subtrair/divisão:")

def numero(n1,n2,option):
     if option=="somar":
        print(n1+n2)
     elif option=="subtrair":
        print(n1-n2)
     elif option=="multiplicar":
        print(n1*n2)
     elif option=="divisão":
        print(n1/n2)
numero(n1,n2,option)

