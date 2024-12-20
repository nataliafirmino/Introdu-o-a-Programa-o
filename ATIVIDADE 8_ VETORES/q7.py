vetor=[]
horario=input('Informe um horário: (HH:MM)')
vetor.append(horario)
vetor=horario.split(':')
hora=int(vetor[0])

if  hora > 12:
    print(f'{hora-12} : {vetor[1]} p.m')

else:
    print(f'{hora} : {vetor[1]} a.m')

