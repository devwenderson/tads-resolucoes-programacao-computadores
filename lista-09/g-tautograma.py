'''
===================================== LÓGICA DO PROBLEMA ====================================
Verificar o início de cada palavra 
 - Como?
   - Transformar uma frase numa lista
     - Cada frase com no mínimo uma palavra
   - Usar o slicing em cada palavra para verificar se todas as letras iniciais são iguais
     - Limite de 20 letras cada palavra

Como separar as palavras em posições numa lista?

Preciso de uma variável de controle para gerenciar a veracidade do tautograma
Sempre verifica a frase com base na primeira letra da frase.
Se alguma primeira letra das palavras for diferente, a tautologia é falsa
============================================================================================
'''

while True:
    frase = input()
    if frase == "*":
        break
    
    palavras = list(frase.split()) # Transforma a frase numa lista de palavras
    eh_tautograma = True
    if len(palavras) > 0:
        letra_palavra_atual = palavras[0][0].lower() # Minúsculo para não dar diferença de case sensitve

        for palav in palavras:
            if palav[0].lower() != letra_palavra_atual: 
                eh_tautograma = False
    
    if eh_tautograma:
        print("Y")
    else:
        print("N")
        
