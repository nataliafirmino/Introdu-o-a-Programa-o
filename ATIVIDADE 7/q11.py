

valorTotal=float(input('Informe o valor da conta: R$'))
pessoas=int(input('Informe a quantidade de pessoas:'))
totalPago=0    
while pessoas>0:
    valorIndividual=float(input('Informe o valor que uma pessoa irá pagar: R$'))
    totalPago+=valorIndividual
    pessoas-=1
    faltaPagar=valorTotal-totalPago
    
    if  faltaPagar==0:
        print('A conta foi totalmente paga!')
    else:
        print(f'A conta não foi totalmente paga. Falta R$: {faltaPagar:}')

