def multiplicar(n1, n2):
    resultado = 0
    for i in range(n2):
        resultado += n1
    return resultado


n1=int(input('Informe o primeiro número inteira:'))
n2=int(input('Informe o segundo número inteira:'))

produto=multiplicar(n1, n2)
print('O resultado da multiplicação é:', produto)
