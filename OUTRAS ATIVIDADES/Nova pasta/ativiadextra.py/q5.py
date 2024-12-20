nome=input('Informe o nome do produto:')
produto=float(input('informe o valor do produto:'))
percentual_desconto=(float(input('Informe o percentual de desconto:')))
valordesconto=produto*(percentual_desconto/100)
valorfinal=produto-valordesconto

print('Nome do produto:', nome)
print('Valor do produto:', produto)
print('Percentual de desconto:',percentual_desconto, '%')
print('Valor do desconto:', valordesconto)
print('Valor a ser cobrado:',valorfinal)