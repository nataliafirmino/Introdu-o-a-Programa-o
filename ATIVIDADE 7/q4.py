celsius=0

print('Tabela de conversão Celsius para Fahrenheit:')
while celsius<=40:
    fahrenheit=(9 * celsius +160) /5
    print(f'{celsius}°C = {fahrenheit:.2f}°F')
    celsius=celsius+1