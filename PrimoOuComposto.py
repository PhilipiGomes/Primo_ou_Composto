import os, time


def divisores(n):
    divisors = [1,n]
    i = 2
    while i < n:
        if n % i == 0:
            divisors.insert(-1,i)
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
    divisores_string = ', '.join(str(i) for i in divisors)
    print(f'{n} - composto, divisores: {divisores_string}')



