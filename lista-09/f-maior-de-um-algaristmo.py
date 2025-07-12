'''
1 - Se o primeiro for maior
2 - Se o segundo for maior
0 - Se ambos forem iguais

-------------------------
n >= 10

m >= 10

while soma1 > 10:
    soma += resto
'''

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    soma1 = n
    soma2 = m

    if n > 9:
        soma1 = 0
        while n > 0:
            ultimo_algarismo = n % 10 # Pega o último algarismo
            soma1 += ultimo_algarismo
            n = n // 10 # Remove o último algarismo
            if soma1 > 9:
                soma1a = soma1
                soma1 = 0
                while soma1a > 0:
                    ultimo_algarismo = soma1a % 10 # Pega o último algarismo
                    soma1 += ultimo_algarismo
                    soma1a = soma1a // 10 # Remove o último algarismo


    if m > 9:
        soma2 = 0
        while m > 0:
            ultimo_algarismo = m % 10
            soma2 += ultimo_algarismo
            m = m // 10
            if soma2 > 9:
                soma2a = soma2
                soma2 = 0
                while soma2a > 0:
                    ultimo_algarismo = soma2a % 10 # Pega o último algarismo
                    soma2 += ultimo_algarismo
                    soma2a = soma2a // 10 # Remove o último algarismo
    
    if soma1 > soma2:
        print(1)
    elif soma2 > soma1:
        print(2)
    else:
        print(0)

    
