vetor=[]
i=0

while i < 5:
    num=int(input('Informe um número:'))
    vetor.append(num)
    i+=1
menor= vetor[0]
i=0
posicao=0
while i < 5:
    if vetor[i] < menor:
        menor=vetor[i]
        pos=vetor.index(menor) +1
    i+=1
print(f' o menor número é {menor} e está na {pos}º posição')


    