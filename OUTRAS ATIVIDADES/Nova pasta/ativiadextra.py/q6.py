numero=int(input('Digite um número intiro de três digitos:'))
digito1=numero//100
digito2=numero//10 % 10
digito3=numero % 10
soma=digito1+digito2+digito3
print('A soma dos digitos é:', soma)