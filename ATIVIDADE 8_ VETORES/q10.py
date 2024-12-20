vetor=[]
i=0
j=None
aux=None

while i < 5:
    numero=int(input('Informe um número:'))
    vetor.append(numero)
    i+=1
i=0
while i < (len(vetor)-1):
    j=i+1
    while (j <  len(vetor)):
        if  vetor[i]  > vetor[j]:   
            aux=vetor[i]
            vetor[i] = vetor[j]
            vetor[j]=aux
        j+=1
    i+=1
print(f'Números impressos de maneira ordenada crescente são: {vetor}')