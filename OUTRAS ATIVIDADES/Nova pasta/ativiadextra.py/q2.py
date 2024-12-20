idade=int(input('Informe sua idade:'))
#o coração bate 1 vez por segundo;entao o coração bate 84600 vezes/segundos por dia
coracao=1*86400
#multiplica por 365 (quantiade de dias que tem um ano) e multiplica pela idade
vezes=365*coracao*idade
print('Se você tem',idade,'anos, seu coração bateu', vezes, 'vezes.')
