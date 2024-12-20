matriz=[]
print('Digite os valores na matriz 3x3:')
for linha in range(3):
    vetor=[]
    for coluna in range(3):
        valor=int(input(f'Informe um número inteiro:'))
        vetor.append(valor)
    matriz.append(vetor)

print('Matriz original:')

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=' ')
    print()


print('Matriz transposta')
for coluna in range(3):
    for linha in range(3):
        print(matriz[linha][coluna], end=' ')
    print()

    