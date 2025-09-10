idade=int(input("Qual a sua idade?"))
estudante=input("É estudante?(sim/não)")


if estudante=="não" and idade<=12:
    print("O valor é de R$8,00")
elif estudante=="não/sim" and idade<65:
    print("O valor é de R$10,00")
elif estudante=="sim" and idade >0 and idade <90:
    print("O valor é de R$12,00")
elif idade>=13 and idade <=64 and estudante=="não":
    print("O valor é de R$20,00")
