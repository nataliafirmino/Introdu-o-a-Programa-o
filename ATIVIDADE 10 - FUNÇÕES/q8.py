#Crie uma função que recebe a idade de um eleitor, e retorna a sua classe eleitoral:
#• não-eleitor (abaixo de 16 anos)
#• eleitor obrigatório (a partir de 18 até 65 anos).
#• eleitor facultativo (16 e 17 anos / maior que 65 anos).

def classeEleitoral(idade):
    if  idade < 16:
        return('Não-eleitor')
    elif    idade <=18 and idade < 65:
        return('Eleitor obrigatório')
    else:
        return('Eleitor acultativo')
    
idade=int(input('Informe a idade:'))
classe=classeEleitoral(idade)
print(f'Para uma pessoa com {idade} anos, a classe eleitoral é: {classe}.')