'''Crie um módulo chamado “vetor”, que disponibilize as seguintes funções
que irão receber um vetor no parâmetro e:
1. exibir: Imprime os elementos em linhas separadas;
2. exibirNumerado: Imprime os elementos com uma ordem numérica ao
lado, em linhas separadas;
3. soma: Retorna a soma dos elementos do vetor;
4. tamanho: Retorna o tamanho do vetor;
5. media: Retorna a média dos elementos (números) do vetor.'''

from vetor import *

numElementos = int(input("Digite o número de elementos do vetor: "))

meuVetor = []

for i in range(numElementos):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    meuVetor.append(elemento)

print('Elementos do vetor:')
exibir(meuVetor)

print('Elementos numerados:')
exibirNumerado(meuVetor)

print(f'Soma dos elementos:{soma(meuVetor)}')
print(f'Tamanho do vetor: {tamanho(meuVetor)}')
print(f'Média dos elementos: {media(meuVetor)}')
