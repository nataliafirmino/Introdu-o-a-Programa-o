#Exiba uma matriz utilizando os valores e formato abaixo:
#9 7 1
#8 3 4
#6 5 2

matriz=[[9,7,1], [8,3,4],[6,5,2]]
for linha in range(3):
    for coluna in range (3):
        print(matriz[linha][coluna],end='')
    print()