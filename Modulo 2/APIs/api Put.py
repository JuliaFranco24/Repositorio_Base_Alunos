import requests
pedido=input("")

pedido={
    'Prato':"pizza de alho",
    "Sobremesa":"Pettit gatteau",
    "Mesa":"4",
    "Bebida":"Suco de Maracujá"
}

pedido=requests.put("https://68dea90a898434f4135597b9.mockapi.io/Restaurante/6",pedido)
