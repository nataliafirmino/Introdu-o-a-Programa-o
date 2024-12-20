vetor=[]
i=0
numero=100
while i < 10:
    if  numero % 2==1:
        vetor.append(numero)
        i+=1
    numero+=1
print(f'os 10 primeiros números ímpares acima de 100 são: {vetor}')