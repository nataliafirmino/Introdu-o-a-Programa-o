#Solicite ao usuário as dimensões de uma matriz (linhas e colunas), e
#monte uma matriz preenchidas com números crescentes, começando
#em 1. Exiba a matriz montada para o usuário. Exemplo:
#Digite quantas linhas na matriz: 3
#Digite quantas colunas na matriz: 2
#1 2
#3 4
#5 6

linha=int(input('Informe a quantidade de linhas:'))
coluna=int(input('Informe a quantidade de colunas:'))
valor=1
matriz=[]
for i in range(linha):
    vlinha=[]
    for j in range(coluna):
        vlinha.append(valor)
        valor+=1
    matriz.append(vlinha)

for i in range(linha):
    for j in range(coluna):
        print(matriz[i][j], end=' ')
    print()