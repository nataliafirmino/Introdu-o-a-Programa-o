valor=float(input('Digite o valor:'))
print('1. à vista (10% de desconto)')
print('2. 1x no cartão (5% de desconto)')
print('3. 2x no cartão (sem desconto/acréscimo)')
print('4. 5x no cartão (10% de acréscimo)')

opcao=input('Escolha um número: 1, 2, 3 ou 4:')
if    opcao=='1':
    valor=valor-valor*(10/100)
    print('O valor a ser pago é: R$', valor)
if    opcao=='2':
    valor=valor-valor*0.05
    print('O valor a ser pago é: R$', valor)
if    opcao=='3':
    valor=valor/2
    print('O valor a ser pago é: R$', valor)
if     opcao=='4':
    valor=((10/100)*valor+valor)/5
    
    
    print('O valor a ser pago é: R$', valor)