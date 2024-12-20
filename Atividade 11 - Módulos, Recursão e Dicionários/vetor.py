
def exibir(vetor):
    for elemento in vetor:
        print(elemento)

def exibirNumerado(vetor):
    i=1
    for elemento in vetor:
        print(f"{i}. {elemento}")
        i+=1

def soma(vetor):
    total=0
    for elemento in vetor:
        total+=elemento
    return total


def tamanho(vetor):
    cont=0
    for i in vetor:
        cont+=1
    return cont

def media(vetor):
    total=0
    cont=0
    
    for elemento in vetor:
        total+=elemento
        cont+=1
    return total/cont
