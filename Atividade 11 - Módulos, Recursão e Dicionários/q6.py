'''Crie um programa que cadastre um cliente de uma loja em um dicionário,
com as seguintes informações passadas pelo usuário: nome, endereço e
telefone.'''

cliente={}

nome=input('Informe o nome:')
endereco=input('Informe o endereço:')
telefone=int(input('Informe o telefone:'))

cliente['nome']=nome
cliente['endereço']=endereco
cliente['telefone']=telefone

print(cliente)
    
