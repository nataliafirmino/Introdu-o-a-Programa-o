#Escrever um algoritmo para solicitar valores inteiros e inserir em uma 
#matriz 2x3. Calcular e imprimir a média dos valores contidos na matriz.
soma=0
contador=0
matriz=[]
for linha in range(2):
    vetor=[]
    for coluna in range(3):
        num=int(input('Informe um número:'))
        contador+=1
        vetor.append(num)
        soma=soma+num
        
    matriz.append(vetor)
    media=soma/contador
print(f'A média dos valores contidos na matrriz é:{media}')