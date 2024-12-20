i=0
nomes=[]
medias=[]
acimadamedia=[]
while i < 5:
    nome=input('Informe o nome:')
    media=float(input('Informe a média:'))
    medias.append(media)
    if  media >= 7:
        nomes.append(nome)
        acimadamedia.append(media)  
    i+=1 
print(f'Parabéns, {nomes}! suas médias {medias} foram acima da turma!')