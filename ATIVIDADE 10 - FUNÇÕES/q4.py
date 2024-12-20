#Crie uma função que receba um número entre 1 e 7, e retorne o nome do dia
#respectivo. Considere o domingo como o primeiro dia.

def nomeDia(numero):
    diasSemana=['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira', 'sexta-feira','Sábado']
    return diasSemana[numero-1 ]#como o dia da semana começa no domingo, subtrai o numero com 1 para dá o resultado correto

numero=int(input('Informe um número entre 1 e 7:'))
nome=nomeDia(numero)#chamando a função
print(f'O dia da semana que corresponde ao numero {numero} é {nome}')