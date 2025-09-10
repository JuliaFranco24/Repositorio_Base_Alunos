#Criador de Saudação Enunciado: Crie uma função que receba um nome e um horário (manhã,tarde, noite) e retorne uma saudação personalizada.
nome=input("Qual o seu nome?")
horario=input("Escolha um período:(manhã/tarde/noite)")

def pergunta(nome,horario):
    if horario=="manhã":
        print("Ola", nome,"Bom dia")
    elif horario=="tarde":
        print("Ola", nome,"Boa tarde")
    elif horario=="noite":
        print ("Ola", nome,"Boa noite")


pergunta(nome,horario)