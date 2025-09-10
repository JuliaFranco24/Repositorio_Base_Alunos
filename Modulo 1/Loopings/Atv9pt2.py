palavra= (input("Digite alguma palavra:"))
contadora=0
numero_de_letras=len(palavra)

for item in palavra:
    print(item)
    if item in 'aeiou':
        print("vogal")
        contadora=contadora+1
    else:
        print("consoante")


print(contadora)