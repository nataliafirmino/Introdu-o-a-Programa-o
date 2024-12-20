'''Considere um sistema para um cadastro de produtos:
1. Crie um vetor vazio chamado de produtos.
2. Crie uma função chamada adicionar, que receba como parâmetros o
nome, preço e data de fabricação de um produto, crie um dicionário a
partir destas informações, e adicione-o ao vetor de produtos.
3. Crie uma função chamada listar, que irá exibir na tela os dados de
todos os produtos, um abaixo do outro.
4. Crie uma função chamada remover, que irá receber como parâmetro
o nome do produto, e o removerá do vetor.'''


produtos = []

def adicionar(nome, preco, dataFabricacao):
    produto = {
        'Nome': 'Coca-Cola',
        'Preço': preco,
        'Data de Fabricação': dataFabricacao
    }
    produtos.append(produto)
    print(f'O produto "{nome}" foi adicionado com sucesso.')


def listar():
    if not produtos:
        print('Não há produtos cadastrados.')
    else:
        print('Lista de Produtos:')
        for produto in produtos:
            print(f'Nome: {produto["Nome"]}, Preço: R${produto["Preço"]}, Data de Fabricação: {produto["Data de Fabricação"]}')


def remover(nome):
    for produto in produtos:
        if produto['Nome'] == nome:
            produtos.remove(produto)
            print(f'O produto "{nome}" foi removido com sucesso.')
            return
    print(f'O produto "{nome}" não foi encontrado.')


adicionar('Coca-Cola', 9.99, '07-09-2021')
adicionar('Havaianas', 49.55, '25-02-2018')

listar()

remover('Coca-Cola')

listar()
