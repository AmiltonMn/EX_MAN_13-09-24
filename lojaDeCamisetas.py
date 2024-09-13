# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/listamold6.c

P = 0
M = 0
G = 0

def valorPedido(P, M, G, nome):
    
    total = (P * 10) + (M * 12) + (G * 15)
    print(f'Olá {nome}!\nO valor total do pedido será de R${total:.2f}')

nome = input('Digite seu nome:\n')
P = int(input('Qual a quantiade de camisetas de tamanho P(RS10,00)?\n'))
M = int(input('Qual a quantiade de camisetas de tamanho M(RS12,00)?\n'))
G = int(input('Qual a quantiade de camisetas de tamanho G(RS15,00)?\n'))

valorPedido(P, M, G, nome)
