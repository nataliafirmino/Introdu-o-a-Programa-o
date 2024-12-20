valorTotal=0
while True:
    print('''
    Produto |   Código | Preço     
    Cachorro-quente' | 100 | R$2,50    
    Bauru  | 101 | R$3,00
    Hamburguer | 102  | R$4,00
    Refrigerante | 103 | R$3,00
    Sair   | 0
        ''')

    
    codigo=int(input('Informe o código:'))
    quantidade=int(input('Informe a quantidade:'))
    if codigo==100:
        valorPedido=2.50*quantidade
        print(valorPedido)
        valorTotal+=valorPedido
    elif codigo==101:
        valorPedido=3.00*quantidade
        print(valorPedido)
        valorTotal+=valorPedido
    elif codigo==102:
        valorPedido=4.00*quantidade
        print(valorPedido)
        valorTotal+=valorPedido
    elif codigo==103:
        valorPedido=3.00*quantidade
        print(valorPedido)
        valorTotal+=valorPedido
    else:
        if codigo==0 and quantidade==0:
           
            print('O valor a ser pago é: R$', valorTotal)
            break
        codigo+=1