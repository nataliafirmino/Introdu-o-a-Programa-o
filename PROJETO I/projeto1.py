from prettytable import PrettyTable 
import time

print('Iniciando progarama...')
time.sleep(5)
print('Programa iniciado!')

matrizDados=[]

while True:
    print(f'''{'-'*65}
    1.  Cadastrar aluno. 
    2.  Exibir dados de um aluno.
    3.  Exibir a média geral dos alunos.
    4.  Exibir o nome do aluno que possui o maior rendimento.
    5.  Remover aluno.
    6.  Gerar relatório de alunos.
    7.  Sair
{'-'*65} ''')

    opcao=int(input('Informe a opção desejada:'))


    if  opcao==1:
        vetorDados=[]
        nome=str(input('Informe o nome do(a) aluno(a):'))
        media=float(input(f'Informe a média do(a) aluno(a) {nome}:'))
        matricula=str(input(f'Informe a matricula do(a) aluno(a) {nome}:'))
        vetorDados.append(nome), vetorDados.append(media), vetorDados.append(matricula)
        matrizDados.append(vetorDados)
        input('Tecle enter para continuar...')

    elif    opcao==2:
        if  len(matrizDados) > 0:
            matriculaAluno=str(input('Informe a maticula do(a) aluno(a):'))
            for linha in range(len(matrizDados)):
                if  matrizDados[linha][2] ==  matriculaAluno:
                    print(f'Dados do aluno:\nNome:{matrizDados[linha][0]}\nMédia: {matrizDados[linha][1]}\nMatricula:{matrizDados[linha][2]}')
                    input('Tecle enter para continuar...')

    elif    opcao==3:
        soma=0
        contador=0
        if  len(matrizDados)>0:
            for linha in range(len(matrizDados)):
                contador+=1
                soma=soma+matrizDados[linha][1]
                
            mediaTurma=soma/contador
            print(f'Média da turma:{mediaTurma:.2f}')

        else:
            print('Não há alunos cadastrados, tente novamente!')
            
        input('Tecle enter para continuar...')


    elif    opcao==4:
        if  len(matrizDados)>0:
            maiorNota=matrizDados[0][1]
            maiorNome=matrizDados[0][0]
            for linha in range(len(matrizDados)):
                if  matrizDados[linha][1] > maiorNota:
                    maiorNota=matrizDados[linha][1]
                    maiorNome=matrizDados[linha][0]
            print(f'Aluno(a) com maior rendimento: {maiorNome}')
            

        else:
            print('Não há alunos cadastrados, tente novamente!')
            
        input('Tecle enter para continuar...')


    elif    opcao==5:
        if  len(matrizDados)>0:
            matriculaAluno=input(f'Informe a matricula do(a) aluno(a) que deseja remover:')
            for linha in range(len(matrizDados)):
                if matrizDados[linha][2] == matriculaAluno:
                    matrizDados.pop(linha)
                    break

        else:
            print('Não há alunos cadastrados, tente novamente!')
            break
        input('Tecle enter para continuar...')

    elif    opcao==6:
        if  len(matrizDados)>0:
            for linha in range(len(matrizDados)):
                tablela=PrettyTable()
                tablela.field_names=(['Nome',  'Média','Matricula'])
                tablela.add_row(matrizDados[linha])
                print(tablela)

        else:
            print('Não há alunos cadastrados, tente novamente!')
        input('Tecle enter para continuar...')


    else:
        if  opcao==7:
            print('aguarde, encerrando  progarama...')
            time.sleep(5)
            break
        else:
            print('Opção inválida, tente novamente!')
        
print(f'Programa encerrado!')




    
                    

 



