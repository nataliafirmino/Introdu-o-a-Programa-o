#Crie um algoritmo que solicita números ao usuário, e preencha uma matriz 3x3.

matriz=[]

for linha in range(3):
    vetor=[]
    for coluna in range (3):
        num=int(input('Informe o número:'))
        vetor.append(num)
    matriz.append(vetor)
print(matriz)