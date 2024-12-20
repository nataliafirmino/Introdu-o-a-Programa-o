i=0
vetor=[]

while i < 10:
    num=int(input('Informe um número:'))
    
    if  num%3==0:
        vetor.append(num)
    i+=1
print(f'Os números com índice múltiplo de 3 é:{vetor}')