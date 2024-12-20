#Crie uma função que receba um vetor de números como parâmetro e
#retorne a média dos números. Não utilize as funções sum e len.
vetor =[]
def calcularMedia(vetor):
    soma=0
    contador=0

    for elemento in vetor:
        soma+= elemento 
        contador+= 1
    media=soma/contador
    return media

tamanhoVetor=int(input('Informe o tamanho do vetor que deseja:'))

for i in range(tamanhoVetor):
    num=int(input('Informe um número:'))
    vetor.append(num)
    
resultado=calcularMedia(vetor)
print(f'A média dos números no vetor é:{resultado}')
