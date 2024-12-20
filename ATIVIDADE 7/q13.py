velocidadeA=10  #m/s
velocidadeB=15  #m/s

comprimentoPista=2000 #metros

posicaoA=0
posicaoB=comprimentoPista
tempo=0
while posicaoA<posicaoB:
    posicaoA=posicaoA+velocidadeA
    posicaoB=posicaoB-velocidadeB
    tempo=tempo+1
print('O tempo necessário para os ciclitas se encotrarem é',tempo,' segundos')