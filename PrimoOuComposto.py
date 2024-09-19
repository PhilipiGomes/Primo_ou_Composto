import os, time

# Função que encontra todos os divisores de n
def divisores(n):
    divisors = [1, n]  # Inicializa com 1 e n como divisores garantidos
    i = 2  # Começa a verificar divisores a partir de 2
    while i < n:
        if n % i == 0:  # Se i divide n, adiciona à lista
            divisors.insert(-1, i)  # Insere o divisor no penúltimo elemento
        i += 1
    return divisors

# Limpa a tela do console
os.system('cls')

# Solicita ao usuário um número maior que 1
n = int(input('Insira um número: '))
while n <= 1:
    print('Insira um número maior que 1')
    time.sleep(3)  # Aguarda 3 segundos antes de repetir a solicitação
    os.system('cls')  # Limpa a tela novamente
    n = int(input('Insira um número: '))

# Obtém os divisores do número inserido
divisors = divisores(n)
os.system('cls')

# Se houver apenas dois divisores (1 e n), o número é primo
if len(divisors) == 2:
    print(f'{n} - primo')
else:
    print(f'{n} - composto, divisores: {divisors}')
