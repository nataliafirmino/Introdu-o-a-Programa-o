tempo=int(input(' Quantos anos você fuma?'))
cigarros=int(input('Quantos cigarros você fuma por dia?'))
preco=float(input('Qual valor de um cigarro?'))
gasto=cigarros*preco*365*tempo

print('Se você fuma por', tempo,'anos, então gastou R$',gasto)