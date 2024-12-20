'''Crie um dicionário que represente um funcionário, com as seguintes
informações: nome -> Josiberto, idade -> 20, salário -> 2000, cpf -> 4896129.
1. Solicite ao usuário o endereço do funcionário, e adicione ao dicionário.
2. Solicite ao usuário o novo salário do funcionário, e atualize o
dicionário.
3. Remova a informação de cpf do funcionário.
4. Exiba na tela o nome e a idade do funcionário.
5. Exiba na tela todos os dados do funcionário (repetição).'''

funcionario={
    'Nome':'Josiberto',
    'Idade':'20',
    'Salário':'R$2000',
    'CPF':'4896129'
}


endereco=input('Informe o endereço de Josiberto:')
funcionario['Endereço']=endereco

#novo salário:
novoSalario=float(input('Informe o novo salário de Josiberto:'))
funcionario['Salário']=novoSalario

#Printar nome e idade:
print(f"{funcionario['Nome']}")
print(f"{funcionario['Idade']}")

#Remover CPF:
funcionario.pop('CPF')
print(funcionario)

#Mostrar nome do funcionário:
for chave in funcionario:
    print(f'{chave}:{funcionario[chave]}')