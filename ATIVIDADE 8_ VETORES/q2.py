vetor=[]
while True:
    nome=input('Informe o nome:')
    cadastro=input('Deseja continuar o cadastro? Digite (SIM/NÃO)')

    if  cadastro=='SIM':
        vetor.append(nome)
    else:
        break
print(f'Os alunos que aceitaram continuar o cadastro foram: {vetor}')