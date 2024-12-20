i=1
contador=0
soma=0
while i!=0:
    numero=int(input('Informe um número:'))
    if numero > 0:
        soma=soma+numero
        print(f'A soma dos numeros positivos é: {soma}')
    elif    numero <0:
        contador=contador+1
        print(f'A quantidade de números negativos é: {contador}')
    else:
        if  numero==0:
            break
    i+=1

