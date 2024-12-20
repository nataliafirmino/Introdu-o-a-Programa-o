'''Crie um módulo chamado “unidades”, que disponibilize funções para
converter unidades. Pesquise, faça as funções que converta, e teste-as:
1. Fahrenheit para Celsius
2. Libras para Quilos
3. Polegadas para Centímetros
4. Milhas para Quilômetros
5. km/h para m/s
6. Pés para Metros'''


from unidades import *

_FahrenheitCelsius  = FahrenheitCelsius(86)

print(f'{86} ºF é: {_FahrenheitCelsius} ºC')

_librasQuilos = librasQuilos(64)
print(f'{64} lb em kg é: {_librasQuilos:.2f}kg')

_polegadaCentimetro = polegadasCentimetros(50)
print(f'{50} in é: {_polegadaCentimetro} cm')

_milhasQuilômetros = milhasQuilômetros(5)
print(f'{5} mi é: {_milhasQuilômetros} km')

_kmParaM = kmParaM(18)
print(f'{18} km/h é: {_kmParaM} m/s')

_pesMetros = pesMetros(115)
print(f'{115} ft é: {_pesMetros:.2f} m')