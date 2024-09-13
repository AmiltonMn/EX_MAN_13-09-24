# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/aulapratica22.c

while True:
    try:
        dias = int(input('Qual a quantidade de dias trabalhados ao mês?\n'))
        horas = int(input('Qual a quantidade de horas trabalhadas por dia?\n'))
        valor = float(input('Qual o valor da hora por dia?\n'))
        break
    except:
        print('Valor inválido!\n')
        pass

print(f'O salário mensal é de {valor*horas*dias}')