#Crie uma função que receba duas notas, calcule a média e retorne se o aluno
#foi APROVADO (>= 6), REPROVADO (< 2) ou RECUPERAÇÃO.

def media():
    nota1=float(input('Informe a nota 1:'))
    nota2=float(input('Informe a nota 2:'))
    return(nota1+nota2)/2
mediaAluno=media()

if  mediaAluno >= 6:
    print('APROVADO')
elif    mediaAluno < 2:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')

