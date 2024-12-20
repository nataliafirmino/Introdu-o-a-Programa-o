# escola.py

nomes = []
notas = []
quantidadeAlunos = 0

def cadastrarAluno(nome, nota):
    global quantidadeAlunos
    nomes.append(nome)
    notas.append(nota)
    quantidadeAlunos += 1
    print(f'Aluno {nome} cadastrado com nota {nota}.')

def buscarNota(nome):
    global quantidadeAlunos 
    for i in range(quantidadeAlunos ):
        if nomes[i] == nome:
            return notas[i]
    return f'Aluno {nome} não encontrado.'

def alunoMaiorNota():
    global quantidadeAlunos 
    if  quantidadeAlunos  == 0:
        return 'Não há alunos cadastrados.'
    else:
        indiceMaxNota = 0
        for i in range(1, quantidadeAlunos ):
            if notas[i] > notas[indiceMaxNota]:
                indiceMaxNota = i
        return nomes[indiceMaxNota]

def mediaGeral():
    global quantidadeAlunos 
    if quantidadeAlunos  == 0:
        return 'Não há alunos cadastrados.'
    else:
        somaNotas = 0
        for i in range(quantidadeAlunos):
            somaNotas += notas[i]
        return somaNotas / quantidadeAlunos 

def imprimirRelacao():
    global quantidadeAlunos
    if quantidadeAlunos == 0:
        print('Não há alunos cadastrados.')
    else:
        print('Relação de Alunos:')
        for i in range(quantidadeAlunos):
            print(f'Nome: {nomes[i]}, Nota: {notas[i]}')
