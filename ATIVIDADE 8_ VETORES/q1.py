i=0
vetor=[]

while i < 5:
    numero=int(input('Digite um número:'))  
    vetor.append(numero)
    i+=1

print('Valores na ordem contrária:')
elemento=len(vetor)-1

while elemento >=0:
    print(vetor[elemento])
    elemento-=1
