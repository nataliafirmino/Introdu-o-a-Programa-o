salario=float(input('Digite seu salário:'))
emprestimo=float(input('Digite o valor o empréstimo:'))
parcela=int(input('Informe a quantidade que deseja de parcelas:'))
juro=0.01 * parcela * emprestimo
valortotal=emprestimo + juro
valorparcela=valortotal / parcela
limitep=0.3*salario

if  valorparcela>limitep:
    print('Empréstimo concedido')
else:
   print('Empréstimo não concedido.')