'''Crie uma função recursiva que calcule uma sequência fibonacci de N
elementos utilizando recursão. Considere a sequência começando em 0 e 1.'''


def fibonacci(n):
    if n == 0:
        return []
    
    elif n == 1:
        return [0]
    
    elif n == 2:
        return [0, 1]
    
    else:
        fib_list = fibonacci(n - 1)

        fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list


n = 10
resultado = fibonacci(n)

print(f'Os primeiros {n} elementos da sequência de Fibonacci são: {resultado}')
