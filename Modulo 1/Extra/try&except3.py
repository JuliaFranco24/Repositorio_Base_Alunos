#Exercício 3: Acesso a Elemento de Lista com Índice
#$Peça ao usuário um índice e tente acessar um elemento em uma lista predefinida (ex: [10,
#20, 30]). Use try-except para tratar IndexError (índice fora do intervalo) e ValueError (se o
#índice não for um inteiro). Exiba mensagens específicas para cada erro.
indice=[10,20,30]


try:
    print(indice[7])
except:
    print('o indice nao existe')
    