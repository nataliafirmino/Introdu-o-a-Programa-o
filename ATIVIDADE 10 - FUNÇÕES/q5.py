#Crie uma função que receba um valor em Celsius e retorne em Fahrenheit.
#Chame a função 20 vezes, passando como parâmetros os valores de 1 à 20, e
#exibindo os respectivos resultados. F = (9 * C + 160) / 5

def temperatura(celsius):
    return(9 * celsius + 160)/5
contador=0
for i in range(1,21):
    contador+=1
    print(f'{contador}°C = {temperatura(i)}°F')