#Crie uma função que valida uma senha enviada pelousuário
senhas=input("Qual é a senha?")

def senha(senhas):
     if senhas=="hamburguer preto":
        print("Acesso liberado")
     else:
        print("Acesso Negado")

senha(senhas)