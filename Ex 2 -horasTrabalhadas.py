# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/aulapratica26.c

try:
    dias = int(input('Digite o número de dias!'))
except:
    print('Valor digitado inválido!')
    
hora = 0
resp = 0
    
for i in range(dias):
    hora = int(input(f'Digite a hora do {i + 1}° dia: \n'))
    resp += hora
    
print(f'A média de horas trabalhadas é de: {resp/dias}h por dia!')