#Imprima em forma de matriz preenchido com 0 de acordo com as dimensões passadas pelo usuário (linhas x colunas).
#Exemplo:
#Digite quantas linhas na matriz: 3
#Digite quantas colunas na matriz: 4
#0 0 0 0
#0 0 0 0
#0 0 0 0

linha=int(input('Informe a quantidade de linhas:'))
coluna=int(input('Informe a quantidade de colunas:'))

matriz=[]
for i in range(linha):
    vlinha=[]
    for j in range(coluna):
        vlinha.append(0)
    matriz.append(vlinha)

for i in range(linha):
    for j in range(coluna):
        print(matriz[i][j], end=' ')
    print()