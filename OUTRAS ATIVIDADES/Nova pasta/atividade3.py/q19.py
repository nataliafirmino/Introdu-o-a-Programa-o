horas_uso=int(input('Informe a quantidade de horas de uso da biciceta:'))
horas=horas_uso//3
horas_adicionais=horas_uso % 3
valor_total=(horas*10)+(horas_adicionais*5)
print('O valor a ser pago é R$:',valor_total)
