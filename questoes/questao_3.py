## QUESTÃO 3 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    c = 0

    b = 0

    e = 0

    d = 0

    def direcao(x):
        global c
        global b
        global e
        global d
        xs = x.split()
        if xs[0] == 'CIMA':
            c += int(xs[1])
        if xs[0] == 'BAIXO':
            b += int(xs[1])
        if xs[0] == 'ESQUERDA':
            e += int(xs[1])
        if xs[0] == 'DIREITA':
            d += int(xs[1])


    while True:
        x = input().upper()
        if x == '':
            break
        else:
            direcao(x)
            continue

    z = ((c - b)**2 + (d - e)**2)**(1/2)
    z = round(z)
    print(z)




    
if __name__ == '__main__':
    main()
