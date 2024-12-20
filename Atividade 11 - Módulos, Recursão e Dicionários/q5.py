'''Crie um módulo chamado “escola”, que disponibilize funções para:
1. Receber o nome de um aluno e sua nota, e guardar as informações em
vetores (um vetor para os nomes, outro para as notas)
2. Receber o nome de um aluno cadastrado e retornar a sua nota
3. Retornar o nome do aluno com a maior nota cadastrada
4. Exibir a média geral dos alunos cadastrados
5. Imprimir a relação completa dos alunos cadastrados e suas notas
No arquivo main crie um sistema de menu com as opções acima, utilizando
as funções do módulo escola.'''

from escola import *

cadastrarAluno('Lua', 7.5)
cadastrarAluno('Tomas', 9.4)
cadastrarAluno('Maya', 8.5)

# Buscar nota de um aluno:
notaMaya= buscarNota('João')
print(f'A nota de João é: {notaMaya}')

print()

melhorAluno = alunoMaiorNota()
print(f'O aluno com a maior nota é: {melhorAluno}')

print()

media = mediaGeral()
print(f'A média geral dos alunos é: {media:.2f}')

print()

imprimirRelacao()


