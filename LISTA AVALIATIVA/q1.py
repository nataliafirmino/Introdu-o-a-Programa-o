num=1000
contador=0

while contador < 5:
    if num % 11==5:
        contador+=1

        if  contador==5:
            print('O quinto número a partir de 1000, que é divisível por 11 com resto 5 é:',num)
            break
    num+=1