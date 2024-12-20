matriz=[['Rafael',1000],  ['Maria', 2000], ['Godofredo',3000],['Josefa', 2500],  ['José',1500]]
maior=matriz[0][1]
i=0
for l in range(len(matriz)):
    if  matriz[l][1] > maior:
        maior=matriz[l][1]
        i=l
print(f'O maior salário é: {matriz[i][0]} - R$ {maior}')