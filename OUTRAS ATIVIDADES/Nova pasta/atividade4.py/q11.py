print('Digite qual seu plano de trabalho:')
plano=input('Digite A, para plano A; B, para plano B, e C, para plano C')
salario=float(input('Digite seu salário:'))
if  plano=='A':
    plano=(salario*0.10+salario)
    print('Seu novo salario será: R$',plano)

if  plano=='B':
    plano=(salario*0.15+salario)
    print('Seu novo salario será: R$',plano)

if  plano=='C':

    plano=(salario*0.20+salario)
    print('Seu novo salario será: R$',plano)
