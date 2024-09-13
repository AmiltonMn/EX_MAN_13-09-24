# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/exer16funcoespara.c

def soma(valor1, valor2):
    soma = valor1 + valor2
    return soma

while True:
    valor1 = int(input('Digite o 1° valor:\n'))
    valor2 = int(input('Digite o 2° valor:\n'))
    
    print(f'A soma entre {valor1} e {valor2} = {soma(valor1, valor2)}')
    
    continuar = int(input('Deseja fazer mais uma soma?\nDigite 1 para continuar ou 0 para sair'))
    
    if continuar == 1:
        pass
    else:
        break