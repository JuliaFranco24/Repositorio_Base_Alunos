import requests


pedido={
    'Prato':"pizza de alho",
    "Sobremesa":"Pettit gatteau",
    "Mesa":"4",
    "Bebida":"Suco de Maracujá"
}



requests.post('https://68dea90a898434f4135597b9.mockapi.io/Restaurante',pedido)