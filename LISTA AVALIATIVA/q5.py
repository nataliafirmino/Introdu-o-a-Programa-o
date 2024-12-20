
numero=int(input('Informe um número:'))

if  numero==2:
    print(f'{numero} é primo')
elif    numero==1 or numero==0:
    print(f'{numero} não é primo')
else:
    if  numero %2 ==0:
       print(f'{numero} não é primo')
    else:
        contador=3
        while contador<numero:
            if  numero%contador==0:
                break
            contador+=2
    if  contador==numero:
        print(f'{numero} é primo')
    else:
        print(f'{numero} não é primo')