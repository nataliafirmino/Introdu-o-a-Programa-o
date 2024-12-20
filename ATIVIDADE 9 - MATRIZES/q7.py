matriz=[]

for alunos in range(3):
    vetor=[]
    for notas in range(5):
        nota=float(input(f'Informe a {notas+1}º nota do {alunos+1}º aluno:'))
        vetor.append(nota)
    matriz.append(vetor)
print(f'A matriz que representa as 5 notas dos 3 alunos da turma é:{matriz}')
