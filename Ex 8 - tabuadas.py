# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/sistematabuadas.c


while True:
    
    tabuada = int(input('Qual tabuada você gostaria de consultar?\n'))
    numMult = int(input('Até que número você gostaria de fazer a multiplicação?\n'))
    
    print(f'O número digitado para ver a tabuada foi {tabuada}\nE a multiplicação vai até {numMult}\n')

    for i in range (numMult):
        print(f'{tabuada} X {i + 1} = {tabuada * (i + 1)}')
        
    continuar = int(input('Digite 1 para sair ou 0 para continuar e consultar outra tabuada\n'))
    
    if continuar == 1:
        break;
    else:
        pass