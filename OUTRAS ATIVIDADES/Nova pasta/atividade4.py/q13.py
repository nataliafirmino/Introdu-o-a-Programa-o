valor=float(input('Digite o valor do produto:'))
estado=input('Digite a sigla do estado: MG para Minas Gerais;SP para São Paulo e RJ, para Rio de Janeiro; PE, para Pernambuco:')

if estado=='MG':
    valor=valor*0.07+valor
    print('O preço final do produto com o acréscimo do estado é:', valor)

if    estado=='SP':
    valor=valor*0.12+valor
    print('O preço final do produto com o acréscimo do estado é:', valor)


if  estado=='RJ':
    valor=valor*0.15+valor
    print('O preço final do produto com o acréscimo do estado é:',valor)

if  estado=='PE':
    valor=valor*0.08+valor
    print('O preço final do produto com o acréscimo do estado é:', valor)
