# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/busca1.c

listValores = []
cont = 0
valor = 0

while True:
    try:
        qtdValores = int(input('Quantos valores você quer adicionar na lista?\n'))
        break
    except:
        print('Valor inválido!\n')
        pass

for i in range(qtdValores):
    while True:
        try:
            valor = int(input(f'Informe o {i + 1}° valor: '))
            listValores.append(valor)
            break
        except:
            print('Valor inválido!\n')
            pass
while True:
    try:
        busca = int(input('Informe um valor para ser procurado: '))
        break
    except:
        print('Valor inválido!\n')
        pass

for i in range(qtdValores):
    if listValores[i] == busca:
        cont += 1
    else:
        pass

print(f'O valor {busca} foi encontrado {cont} vezes!')