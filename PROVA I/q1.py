velocidade=float(input('Informe a velocidade:'))

if  velocidade >= 80:
    multa=(velocidade-80) *10
    print(f'voce foi multado. O valor da multa é: R$ {multa}')