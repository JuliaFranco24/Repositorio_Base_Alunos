print("Controle de estoque:\n(1) Adicionar unidades ao estoque\n(2) Remover unidades do estoque\n(3) Verificar estoque atual\n(4) Sair")


total=50 
while True:
    option=input('Digite alguma das opções: ')
    if option=='1':
       unidades=int(input("Valor:"))
       total=total+unidades
       print("Unidades adicionadas com sucesso!")
    elif option=='2':
        remover=int(input("Valor para remover:"))
        total=total-remover
        print('O valor foi depositado')
    elif option=='3':
        print("Estoque Atual",total)
    elif option=='4':
        print(input("Obrigado por usar nossos serviços!"))
        break

