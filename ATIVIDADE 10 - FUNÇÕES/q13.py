def funcaoMin(vetor):
    contador=0
    menor=vetor[contador]  
    for elemento in vetor:
        if elemento < menor:
            menor=elemento
            contador+=1
    return menor

tamanhoVetor=int(input('Informe o tamanho do vetor que deseja:'))

vetor=[]
for i in range(tamanhoVetor):
    num=int(input('Informe um número inteiro:'))
vetor.append(num)

menorNum=funcaoMin(vetor)
print("O menor número no vetor é:", menorNum)
