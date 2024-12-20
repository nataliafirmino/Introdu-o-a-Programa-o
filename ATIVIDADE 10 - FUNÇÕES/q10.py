#Crie a sua própria função len (tamanho), que recebe um vetor como
#parâmetro e retorna o seu tamanho. Não utilize a função len.

def funcaoLen(vetor):
    cont=0
    for elemento in vetor:
        cont+=1
    return cont

tamanhoVetor=int(input('Informe o tamanho do vetor que deseja:'))

vetor=[]
for  i in range(tamanhoVetor):
    num=int(input('Informe o número:'))
    vetor.append(num)
    
resultamanho= funcaoLen(vetor)
print(f'O tamanho da lista é:{resultamanho}')




