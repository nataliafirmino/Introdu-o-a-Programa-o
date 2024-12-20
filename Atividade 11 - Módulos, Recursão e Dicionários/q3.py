'''Crie um módulo “banco”, que possua um saldo zero e as seguintes funções:
1. Depositar – Recebe o valor para depósito e adiciona ao saldo;
2. Sacar – Recebe o valor para saque como parâmetro e retorna
verdadeiro, caso consiga sacar, ou falso, em caso de não sacar;
3. Saldo – Retorna o valor do saldo
No arquivo main crie um sistema de menu com as opções acima, utilizando
as funções do módulo banco.'''

from banco import *
while True:
    print('''
    1. Depositar.
    2. Sacar.
    3. Saldo.
        ''')
    opcao=int(input('Informe a opção desejada:'))
    if  opcao==0:
        break

    elif  opcao==1:
        valor=float(input('Informe o valor que deseja depositar:'))
        depositar(valor)
    
    elif    opcao==2:
        valor=float(input('Informe o valor que deseja sacar:'))
        resultado = sacar(valor)
        if  resultado==False:
            print('Saldo insuficiente')

    elif  opcao==3:
            resultado=visualizarSaldo()
            print(f'seu saldo é de: R${resultado}')

    else:
         print('Opção inválida, tente novamente!')
