sb=float(input('Digite seu salário:'))
p=sb*8.5/100
ir=sb*27.5/100
sl=sb-p-ir
print('Com todos os descontos descontados: previdência R$',p,'e Imposto de renda: R$', ir, 'O salário líquido será de: R$',sl)