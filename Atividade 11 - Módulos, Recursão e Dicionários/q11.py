'''Crie uma função recursiva para calcular uma potência, recebendo a
base e o expoente.'''

def calcularPotencia(base, expoente):
    if expoente == 0:
        return 1

    else:
        return base * calcularPotencia(base, expoente - 1)


base = 2
expoente = 3
resultado = calcularPotencia(base, expoente)

print(f'{base}^{expoente} = {resultado}')
