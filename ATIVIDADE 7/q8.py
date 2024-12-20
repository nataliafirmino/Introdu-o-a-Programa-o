dentrodamedia=0
abaixodamedia=0
contador=0
while contador < 5:
    media=float(input(f'Informe a média do aluno contador+1:'))

    if  media < 7:
        dentrodamedia+=1
   
    else:
        abaixodamedia+=1

    contador+=1

print(f'Alunos abaixo da média: {abaixodamedia}')
print(f'Alunos acima da média: {dentrodamedia}')
