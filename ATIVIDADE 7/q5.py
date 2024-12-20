soma=0
contador=1

while True:
    multiplo=7*contador

    if  multiplo<1000:
        soma+=multiplo
        contador+=1
    else:
        break
print(f'A soma dos múltiplos de 7 inferiores a 1000 é: {soma}')