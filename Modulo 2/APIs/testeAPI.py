import requests

# Escolhas=input("Qual prato você deseja escolher?")
# escolha=input("Qual sobremesa você quer?")
# Escolha1=input("Qual bebida você quer?")
# Escolha=input("Qual mesa você deseja ficar?")
# print(Escolhas,Escolha1, escolha,Escolha)

while True:
    dados=requests.get("https://68dea90a898434f4135597b9.mockapi.io/Restaurante")
    option = input(   ' digite uma opçao\n 1 para add\n 2 para deletar\n 3 para changes\n')

    if option =='1':

        Escolhas=input("Qual prato você deseja escolher?")
        escolha=input("Qual sobremesa você quer?")
        Escolha1=input("Qual bebida você quer?")
        Escolha=input("Qual mesa você deseja ficar?")
        print(Escolhas,Escolha1, escolha,Escolha)

        pedido={
            "Prato": Escolhas,
        "Sobremesa": escolha,
        "Mesa": Escolha,
        "Bebida":Escolha1,
        }
        requests.post("https://68dea90a898434f4135597b9.mockapi.io/Restaurante",pedido)
    elif option=='2':
        
        dados = requests.get('https://68c941b9ceef5a150f641654.mockapi.io/Restaurante')

        result = dados.json()


        for item in result:
            print(item.get('id'))



        id = input('digite o id do pedido para deletar ')
        requests.delete(f"https://68dea90a898434f4135597b9.mockapi.io/Restaurante/{id}")    

    elif option=='3':
        dados = requests.get('https://68c941b9ceef5a150f641654.mockapi.io/Restaurante').json()
            
            
        for item in dados:
             id=print(item.get('id'))
        print('vi que voce pediu errado por favor insira o novo pedido')

        id1 = input('digite o numero do id para alteramos o seu pedido')
        Escolhas=input("Qual prato você deseja escolher?")
        escolha=input("Qual sobremesa você quer?")
        Escolha1=input("Qual bebida você quer?")
        Escolha=input("Qual mesa você deseja ficar?")
        pedido1={
                        "Prato": Escolhas,
                        "Sobremesa": escolha,
                        "Mesa": Escolha,
                        "Bebida":Escolha1,
                        }
        requests.put(f'https://68dea90a898434f4135597b9.mockapi.io/Restaurante/{id1}',pedido1)

    break