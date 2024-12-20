def potencia(base, expoente):
    resultado = 1
    for i in range(expoente):
        resultado *= base
    return resultado


base=int(input('Informe o número que representa a base:'))
expoente=int(input('Informe o número que representa o expoente:'))
resultado=potencia(base, expoente)
print("O resultado da potência é:", resultado)
