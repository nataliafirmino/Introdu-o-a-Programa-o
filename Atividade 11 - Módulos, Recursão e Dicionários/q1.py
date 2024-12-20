'''Crie um módulo chamado “volumes”, que disponibilize funções para
calcular o volume do: cubo, paralelepípedo, cilindro, esfera, cone e pirâmide
(base quadrada). Crie um arquivo, importe o módulo e teste as funções.'''

from  volume import *
_Cubo = Cubo(3)
print(f'Volume do cubo: {_Cubo} M³')

_Paralelepipedo = Paralelepipedo(3,2,3)
print(f'Volume do paralelepípedo: {_Paralelepipedo} M³')

_Cilindro = Cilindro(3, 4)
print(f'Volume do cilindro: {_Cilindro} M³')

_esfera = Esfera (2)
print(f'Volume da esfera: {_esfera:.2f} M³')

_cone = Cone(2,3)
print(f'Volume do cone: {_cone:.2f} M³')

_piramide = Piramide(4,2)
print(f'Volume da pirâmide: {_piramide:.2f} M³')