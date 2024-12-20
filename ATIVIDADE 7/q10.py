
numero=int(input('Informe um número inteiro:'))
maior = numero  
menor = numero  

i=1

while i < 4:
    numero = int(input("Digite um número inteiro: "))
    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    i += 1
print('O maior número é:', maior)
print('O menor número é:', menor)
