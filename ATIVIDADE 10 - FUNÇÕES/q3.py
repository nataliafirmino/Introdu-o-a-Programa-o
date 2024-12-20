#Escreva uma função comparar que receba dois números inteiros e retorne o menor número.
def comparar (n1,n2):

    if n1 < n2:
        return n1
    else:
        return n2
    
n1=int(input('Informe o primeiro numero:'))
n2=int(input('Informe o segundo numero:'))
menor=comparar(n1,n2)
print(f'O menor número entre {n1} e {n2} é: {menor}')
