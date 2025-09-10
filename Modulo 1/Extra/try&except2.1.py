#Exercício 2: Divisão com Tratamento de Múltiplas Exceções
#Crie uma função chamada dividir(a, b) que retorne o resultado da divisão a / b.
#Utilize um bloco try-except genérico (sem especificar o tipo de exceção) para tratar
#quaisquer erros que possam ocorrer durante a operação (como divisão por zero ou tipos inválidos).
#Em caso de erro, a função deve retornar None.

n=input("Digite um número para dividir")
n1=input("Digite outro número:")

try:
    n=int(n)
    n1=int(n1)

    print(f"A divisão dos números é: {n/n1}")
except:
    print(None)
