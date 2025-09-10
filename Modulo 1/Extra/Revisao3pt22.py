print("Caixa eletrônico:\n(1) Sacar\n(2) Depositar\n(3) Ver Saldo\n(4) Sair")


total=1000
while True:
    option=input('Digite alguma das opções: ')
    if option=='1':
       saque=int(input("Valor:"))
       total=total-saque
       print("Saque realizado com sucesso!")
    elif option=='2':
        deposito=int(input("Valor para depositar:"))
        total=deposito+total
        print('O valor foi depositado')
    elif option=='3':
        print("Seu Saldo:",total)
    elif option=='4':
        print(input("Obrigado por usar nossos serviços!"))
        break