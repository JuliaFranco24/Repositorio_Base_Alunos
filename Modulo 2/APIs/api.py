import requests

dados=requests.get("https://api.chucknorris.io/jokes/random")


print(dados.json())  