#1. Esta atividade vai trabalhar os comandos Try except e também o comando open()
#para criação do arquivo o intuito é tentar realizar a leitura do arquivo caso ele não
#exista você deve tratar este erro criando o arquivo.
#Passo a passo:
# Usando os conceitos de Try e Except tente fazer a leitura de um arquivo usando o comando.
# with open('nome do arquivo', 'modo') as arquivo:
# variavel = arquivo.modo('conteudo que voce quer inserir')
# print(variavel)
# agora é com você , de forma criativa trate o erro usando Except
# OBS: as palavras variável ,modo e nome do arquivo devem ser substituídas 😉

nome=input("Digite seu nome:")
email=input("Digite seu e-mail:")

try:
     with open('Arquivo de Manipulação','r') as arquivo:
        arquivo.read()


except:
     with open('Arquivo de Manipulação', 'a') as arquivo:
        arquivo.write(nome+"|"+email+ "\n")
     