#Escreva uma função media que receba duas notas de um aluno e retorne a sua média aritmética.

def media():
    nota1=float(input('Informe a nota 1:'))
    nota2=float(input('Informe a nota 2:'))
    return(nota1+nota2)/2
mediaAluno=media()
print(f'A média do aluno é: {mediaAluno}')