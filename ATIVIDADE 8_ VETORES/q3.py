vetor=[]
i=0
soma=0

while i < 5:
    num=int(input(f'Informe {i+1}º número:'))
    vetor.append(num)
    soma=soma+num
    i+=1
print(f'O resultado da soma dos numeros é: {soma}')