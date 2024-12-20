consumo=float(input('Informe seu consumo:'))

if  consumo<=10:
    valorTotal=consumo*5
    print(f'voce consumiu {consumo}kw. O valor total a ser pago é: R${valorTotal}')

elif    consumo > 10 and consumo <= 30:
    valorTotal=consumo*7
    print(f'voce consumiu {consumo}kw. O valor a ser pago é: R$ {valorTotal}')


elif consumo>30:
    valorTotal=consumo*10
    print(f'Voce consumiu {consumo}kw. O valor a ser pago é: R${valorTotal} ')

