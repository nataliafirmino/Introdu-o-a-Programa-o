#Solicite ao usuário o nome e idade de 5 pessoas, organizando as informações em uma matriz.

matriz=[]
nomes=[]
idades=[]
for nome in range(5):
    nome=input(f'Informe o {nome+1}º nome:')
    nomes.append(nome)
matriz.append(nomes)
for idade in range(5):
    idade=int(input(f'Informe a {idade+1}º idade:'))
    idades.append(idade)
matriz.append(idades)

print(matriz)