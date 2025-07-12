'''
Verificar quantas vitórias tem cada jogador

A cada R jogadas, cada jogador acumula uma quantidade de pontos

Para identificar a posição da pontuação de cada jogador: 
    (índice da rodada + qtd_jogadores) % qtd_jogadores 
        O resto dessa divisão será o número do jogador relacionado à pontuação

'''

qtd_jogadores, r = map(int, input().split())
rodadas = list(map(int, input().split()))
maior_vitoria = 0
vitoria_na_rodada = 0
jogador_vencedor = 0

for n_jogador in range(qtd_jogadores):
    for i in range(len(rodadas)):
        if (i + qtd_jogadores) % qtd_jogadores == n_jogador: 
            vitoria_na_rodada += rodadas[i]
    
    if vitoria_na_rodada >= maior_vitoria:
        maior_vitoria = vitoria_na_rodada
        jogador_vencedor = n_jogador + 1
    
    vitoria_na_rodada = 0

print(jogador_vencedor)


