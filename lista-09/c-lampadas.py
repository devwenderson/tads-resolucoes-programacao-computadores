'''
===================================== LÓGICA DO PROBLEMA ===================================
Lâmpadas começas apagadas
 - A = False
 - B = False

Analisar primeiro o interruptor 1
Depois interruptor 2

Alterar o estado das lâmpadas é o mesmo de negar o estado atual delas
Se apertar o interruptor 1, a lampada A será afetada, ou seja, not(lampada_a)
Se apertar o interruptor 2, afetará as duas, ou seja, not(lampada_a) e not(lampada_b)
============================================================================================
'''



'''
===================================== OUTRA FORMA DE FAZER ===================================
n = int(input())
sequencia_cliques = list(map(int, input().split()))

mudancas_lamp_1 = 0
mudancas_lamp_2 = 0

for i in sequencia_cliques:
    if i == 1:
        mudancas_lamp_1 += 1
    if i == 2:
        mudancas_lamp_1 += 1
        mudancas_lamp_2 += 1

if mudancas_lamp_1 % 2 == 0: 
    print(0)
else:
    print(1)

if mudancas_lamp_2 % 2 == 0:
    print(0)
else:
    print(1)
============================================================================================
'''

n = int(input())
sequencia_cliques = list(map(int, input().split()))

lamp_a_acesa = False
lamp_b_acesa = False

for i in sequencia_cliques:
    if i == 1:
        lamp_a_acesa = not(lamp_a_acesa)
    if i == 2:
        lamp_a_acesa = not(lamp_a_acesa)
        lamp_b_acesa = not(lamp_b_acesa)

if lamp_a_acesa:
    print(1)
else:
    print(0)

if lamp_b_acesa:
    print(1)
else:
    print(0)

    