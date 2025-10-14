import requests
prato= input('Qual o prato q vc quer?')
Sobremsa= input('Qual o sobremesa q vc quer?')
Mesa= input('Qual mesa q é vc?')
Bebida= input('Qual bebida q vc quer?')

pedido={
    'Prato': prato,
    "Sobremesa": Sobremsa,
    "Mesa": Mesa,
    "Bebida": Bebida
}



requests.post('https://68dea90a898434f4135597b9.mockapi.io/Restaurante',pedido)