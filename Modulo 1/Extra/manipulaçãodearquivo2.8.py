#Agenda de Contatos
#Implemente um programa que crie e gerencie um arquivo chamado contatos.txt.
#Cada contato deve ter nome, telefone e e-mail.
#O programa deve:
#Permitir cadastrar novos contatos.
#Exibir todos os contatos cadastrados.
#OBS: Neste caso só iremos usar o os comandos de With , open e os modos de leiturae escrita da função open()


nome=input("Digite seu nome:")
email=input("Digite seu e-mail:")
telefone=input("Digite seu telefone:")

with open('Arquivo de Contatos','a') as arquivo:
     conteudo= arquivo.write(nome+ '|'+email+'|'+telefone+'\n')
      


with open('Arquivo de Contatos', 'r') as arquivo:
 julia=arquivo.read()

 print(julia)