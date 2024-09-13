# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/if04.c

tempo = 0
valor = 0

tempo = int(input('Informe o tempo de fidelidade (Em anos):\n'))
valor = float(input('Qual o valor gasto na compra?\n'))

if tempo > 5:
    if valor > 5000:
        print(f'Você terá um desconto de 20%!\nO valor total da sua compra será de {valor - (valor * 0.20)}')
    
    if valor > 1000:
        print(f'Você terá um desconto de 10%!\nO valor total da sua compra será de {valor - (valor * 0.10)}')
    else:
        print('Você não receberá desconto!')
else:
    print('Você não receberá desconto!')
            