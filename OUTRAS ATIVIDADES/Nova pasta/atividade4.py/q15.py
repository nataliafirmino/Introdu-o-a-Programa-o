
print('Cardapio - Código')
print('100 - Cachorro quente')      
print('101 - Bauru Simples')
print('102 - Hamburguer')
print('103 - Refrigerante')
codigo=int(input('Digite o código: 100, 101, 102, 103'))
quantidade=int(input('Digite a quantidade:'))

if  codigo==100:
    valor=5


if  codigo==101:
    valor=6
    

if  codigo==102:
    valor=8.50
    
    
if  codigo==103:
    valor=4

print('O valor a se pago será: R$',(valor*quantidade))
   