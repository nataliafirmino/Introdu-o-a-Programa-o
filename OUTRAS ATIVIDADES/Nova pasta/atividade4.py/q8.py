peso=float(input('Digite seu peso:'))
altura=float(input('Digie sua altura em metros:'))
sexo=input('Digite M para masculino e F para feminino:')
Masculino=peso = 72.7 * altura - 58
Feminino=peso = 62.1 * altura - 44.7
if  sexo=='M':
    print(Masculino)
if  sexo=='F':
    print(Feminino)