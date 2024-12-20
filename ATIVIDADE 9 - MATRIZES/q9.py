matriz=[]

for linha in range(6):
    vetor=[]
    for coluna in range(3):
        num=int(input('Informe um número:'))
        vetor.append(num)
    matriz.append(vetor)

maior=matriz[0][0]
menor=matriz[0][0]

linhaMenor=1
linhaMaior=1
colunaMenor=1
colunaMaior=1

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if (matriz [linha][coluna] > maior):
            maior=matriz[linha][coluna]
            linhaMaior=linha+1
            colunaMaior=coluna+1
    
else:
    if  (matriz[linha][coluna] < menor):
        menor=matriz[linha][coluna]
        linhaMenor=coluna+1
        colunaMenor=coluna+1
    
print(f'o maior elemento é: {maior} na {[linhaMaior]}x{[colunaMaior]}º posição')    
print(f'o menor elemento é: {menor} na {[linhaMenor]}x{[colunaMenor]}º posição')




