import os, time


def divisores(n):
    divisors = []
    i = 1
    while i < n + 1:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors

os.system('cls')
n = int(input('Insira um número: '))
while n <= 1:
    print('Insira um número maior que 1')
    time.sleep(3)
    os.system('cls')
    n = int(input('Insira um número: '))
    
divisors = divisores(n)
os.system('cls')
if len(divisors) == 2:
    print(f'{n} - primo')
else:
    print(f'{n} - composto, divisores: {divisors}')


