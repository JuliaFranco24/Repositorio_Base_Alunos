import requests

dados=requests.get("https://68dea90a898434f4135597b9.mockapi.io/Restaurante")

result=dados.json()

print(result)

for i in result:
    print(i.get("Prato"))
    print(dados.json().get("Sobremesa"))
    print(dados.json().get("Mesa"))
    print(dados.json().get("Bebida"))