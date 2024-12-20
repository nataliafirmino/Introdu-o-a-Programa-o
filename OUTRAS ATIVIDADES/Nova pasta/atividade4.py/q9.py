produto=float(input('Digite o valor do produto:'))
if  produto <100:
    produto=produto*0.4+produto
else:
    produto>100
    produto=produto*0.3+produto
print('O poduto foi vendido por: R$', produto)