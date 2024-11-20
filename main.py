# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.

import random

naipes = ["♠", "♥", "♦", "♣"]
valores = ["A", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"J" ,"Q" ,"K"]
valor_coringa = ["coringa"]
def gerar_baralho(quantidade_baralho, embaralhar = False, coringa=False):

    baralho = []
    while quantidade_baralho > 0:

        for naipe in naipes:
            for valor in valores:
                baralho.append(f'{valor}{naipe}')

        if coringa == True:
            for valor in valor_coringa:
                baralho.append({valor_coringa})

        if embaralhar == True:
            random.shuffle(baralho)
        quantidade_baralho = quantidade_baralho - 1
    print(baralho)

quantidade_baralho = 3
embaralhar = True
com_coringa = True
valor_com_coringa = True if com_coringa
gerar_baralho(quantidade_baralho, embaralhar = False, coringa = False)