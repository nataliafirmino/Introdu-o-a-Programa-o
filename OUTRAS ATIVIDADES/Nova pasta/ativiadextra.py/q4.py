
CandidatoA=int(input('Informe a quantidade de votos do candidato A:'))
CandidatoB=int(input('Informe a quantidade de votos do candidato B:'))
CandidatoC=int(input('Informe a quantidade de votos do candidato C:'))
nulos=int(input('Informe a quantidade de votos nulos:'))
brancos=int(input('Informe a quantidade de votos brancos:'))
votostotais=(CandidatoA+CandidatoB+CandidatoC+brancos+nulos)



print('os votos do candidto A foram:',CandidatoA/votostotais*100, '%')
print('os votos do candidto B foram:', CandidatoB/votostotais*100, '%')
print('os votos do candidto C foram:',CandidatoB/votostotais*100, '%')
print('Os votos não válidos foram:', brancos+nulos/votostotais*100, '%')