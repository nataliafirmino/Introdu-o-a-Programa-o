print('------------------------------')
print('Bem=vindo! \n\nSaldo inicial: R$1000')
print('------------------------------')
print('MENU')
print('----------')
print('1. depósito\n2. saque')
print('Selecione a opção desejada:')
opcao=input('1 para depósito 2 para saque:')
saldo=float(input('Digite o valor:'))


if  opcao=='1':
    saldo=1000+saldo
    print('Depósito efetuado. Novo saldo:', saldo)

else:
    opcao=='2'
    saldo=1000-saldo
    print('Saque efetuado com sucesso. Novo saldo:',saldo)
