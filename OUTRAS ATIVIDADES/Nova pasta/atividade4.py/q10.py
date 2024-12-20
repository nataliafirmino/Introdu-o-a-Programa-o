conta=float(input('Digite o valor da conta:'))
amigos=float(input('Digite a quantidade de amigos:'))
garcom=(input('Vai pagar os 10% para o garçom? Digite S para sim e N para não'))

if  garcom=='S':
    valor=(conta*0.10+conta) / amigos
    print('O valor a ser pago por cada amigo com os 10% do garçom é:', valor)
else:
    garcom=='N'
    valor=conta/amigos
    print('O valor a ser pago pelos amigos sem os 10% do garcomm é:', valor)