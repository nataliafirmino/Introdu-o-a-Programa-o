'''Considere uma aplicação para uma agenda telefônica:

1. Crie um dicionário que represente a agenda telefônica acima.
2. Crie uma função chamada exibir, que recebe como parâmetro o nome
de um contato da agenda, e exibe na tela o telefone dele.
3. Crie uma função chamada listar, que exibirá na tela todos os contatos
e os seus respectivos telefones, em linhas separadas.
4. Crie uma função chamada adicionar, que receba como parâmetros o
nome do contato e o número do telefone, e adicione-o ao dicionário.
Caso o contato já exista, o número será atualizado.
5. Crie uma função chamada remover, que recebe como parâmetro o
nome de um contato da agenda, e o remove. Caso o contato exista na
agenda, retorne verdadeiro, caso contrário, retorne falso.'''

agenda={
    'Rafael':'(87)99147-8812',
    'José':'(81)98122-3201',
    'Maria':'(84)99912-9233',
    'Godofredo':'(87)98181-7390',
    'Jessicleide':'(81)99210-6521'
}

def exibir(nome):
    if nome in agenda: 
        print(f'Telefone de {nome} : {agenda[nome]}')
    else:
        print(f'{nome} não encontrado na agenda.')



def listar():
    print('Lista de contato:')
    for nome in agenda:
        print(f'{nome} : {agenda[nome]}')



def adicionar(nome, telefone):
    agenda[nome]=telefone
    print(f"Contato {nome} adicionado/atualizado com sucesso.")

    
def remover(nome):
    if nome in agenda:
        telefone = agenda.pop(nome, None)
        print(f"Contato {nome} removido.")
        return True
        
    else:
        print(f"Contato {nome} não encontrado na agenda.")
        return False
    
    


listar()

print()

exibir('Godofredo')

print()

adicionar('Natalia', '(83)99814-9367')

print()

remover('Maria')

print()

listar()