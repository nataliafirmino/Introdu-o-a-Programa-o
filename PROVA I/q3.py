i=1
turma=1 
while i<=2:
    nota=float(input('Informe a nota:'))
    media=(nota+nota)/2
    print(media)
    i+=1      
while turma<=5:  
    if media>=7:
        print('APROVADO')
    elif  media <2:
        print('REPROVADO') 
    else:
        if  media >2 and media <7:
            print('RECUPERAÇÃO')
    turma+=1
            
  