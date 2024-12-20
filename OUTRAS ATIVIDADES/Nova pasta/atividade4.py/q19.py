n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))

menor=n1

if    n2<menor:
    menor=n2
    
if    n3<menor:
    menor=n3

print('o menor número é:', menor)