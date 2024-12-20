numeroSecreto=321
tentativas=0
while True:
    palpite=int(input('Informe o número secreto:'))
    tentativas+=1
    if  palpite==numeroSecreto:
        print(f'Parabens, você acertou!\nNúmero de tentativas: {tentativas}')
        break
   
    elif  palpite<numeroSecreto:
            print(f'O número secreto é maior do que o seu palpite: {palpite}')
    else:
            print(f'O número secreto é menor do que o seu palpite: {palpite}')