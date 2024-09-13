# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listalaco_sexoaltura.c

qtdPessoas = int(input('Quantas pessoas serão comparadas?\n'))

somaAlturaTurma = 0
maiorAltura = 0
menorAltura = 1000

somaAlturaHomens = 0
maiorAlturaHomens = 0
qtdHomens = 0

somaAlturaMulheres = 0
maiorAlturaMulheres = 0
qtdMulheres = 0

for i in range(qtdPessoas):
    genero = int(input('Qual o seu gênero? (1) Masculino (2) Feminino\n'))
    altura = float(input('Qual a sua altura?\nExemplo: 1.62\n'))
    somaAlturaTurma += altura

    
    if altura > maiorAltura:
        maiorAltura = altura
        
    if altura < menorAltura:
        menorAltura = altura
    
    if genero == 1:
        somaAlturaHomens += altura
        qtdHomens += 1
        if altura > maiorAlturaHomens:
            maiorAlturaHomens = altura
            
    elif genero == 2:
        somaAlturaMulheres += altura
        qtdMulheres += 1
        if altura > maiorAlturaMulheres:
            maiorAlturaMulheres = altura
            
print('______________________________')
print('_         Resultados         _')
print('______________________________')
print(f'A média de altura das mulheres é de {somaAlturaMulheres / qtdMulheres}')
print(f'A média de altura dos homens é de {somaAlturaHomens / qtdHomens}')
print(f'A média de altura da turma é de {somaAlturaTurma / qtdPessoas}')
print(f'A maior altura da turma é de {maiorAltura}')
print(f'A menor altura da turma é de {menorAltura}')