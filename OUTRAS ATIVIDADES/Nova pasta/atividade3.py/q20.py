valor=int(input('Informe o valor em reais:'))
n100=valor//100
valor%=100
n50=valor//50
valor%=50
n10=valor//10
valor%=10
n1=valor
print('O número de cédulas de R$100 é: ', n100)
print('O número de cédulas de R$50 é:', n50)
print('O número de cédulas de R$10 é:', n10)
print('O número de cédulas de R$1 é:',n1)
