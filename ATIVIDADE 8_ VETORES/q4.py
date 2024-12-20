i=0
notas=[]
soma=0
while i < 5:
    nota=float(input('Informe a nota:'))
    notas.append(nota)
    soma=soma+nota
    media=soma/len(notas)
    i+=1
print(f'a média das notas informadas é: {media}')