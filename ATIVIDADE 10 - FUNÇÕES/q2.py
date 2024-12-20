#Crie uma função que receba o raio de um círculo e retorne a área do círculo.
#Solicite ao usuário o raio, chame a função e exiba o resultado.

def area(raio):
    return(3.14*(raio**2))
raio=float(input('Informe o raio:'))
resultado=area(raio)
print(f'A área do circuolo é:{resultado}')