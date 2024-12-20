#sequência: 0, 1, 1, 2, 3, 5, 8,
13, 21, 34
n1=0
n2=1
i=1

while i<=18:
    aux=n1+n2 #Criação de uma variável auxiliar para armazenar os valores e assim fazer a soma, sem perder o valor anterior.
    print(aux)

    n1=n2
    n2=aux

    i+=1
    