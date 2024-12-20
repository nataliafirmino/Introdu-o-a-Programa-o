#Crie uma função que receba o peso e a altura de uma pessoa, e retorna em qual
#classificação ela está, de acordo com o cálculo do IMC:

def classificacao(imc):
    if  imc < 18.6:
        return('ABAIXO DO PESO')
    
    elif    imc >= 18.6 and imc <=24.9:
        return('PESO IDEAL\nPARABÉNS!')
    
    elif    imc >=25 and imc <=29.9:
        return('LEVEMENTE ACIMA DO PESO')
    
    elif    imc >=30 and imc <=34.9:
        return('OBESIDADE GARAU I')
    
    elif    imc >=35 and imc <=39.9:
        return('OBESIDADE GARAU II (SEVERA)')
    else:
        return('OBESIDADE III(MÓRBIDA)')
    
peso=float(input('Informe o peso:'))
altura=float(input('Informe a altura:'))
imc=peso/(altura**2)

classe=classificacao(imc)
print(f'Pesando {peso}kg, e altura de {altura}m, sua classsificação é: {classe}')