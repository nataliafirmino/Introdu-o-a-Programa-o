#Crie a sua própria função sum (soma), que recebe um vetor de números
#como parâmetro e retorna a soma deles. Não utilize a função sum.

def funcaoSoma(vetor):
    resultado = 0
    for elemento in vetor:
        resultado += elemento
    return resultado

tamanhoVetor=int(input('Informe o tamanho do vetor que deseja:'))
vetor=[]
for i in range(tamanhoVetor):
    num=int(input('Informe um numero inteiro'))
    vetor.append(num)
somaVetor=funcaoSoma(vetor)
print(f'A soma dos elementos do vetor é:{somaVetor}')
