# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica05.c

numPessoas = 0
continuar = 1

while continuar == 1:
    
    nome = str(input('Qual o nome da pessoa?\n'))
    
    altura = float(input('Qual a altura da pessoa?\nExemplo de formato: 1.60\n'))

    sexo = str(input('Qual o sexo da pessoa?(M)Masculino (F)Feminino\n'))
    
    numPessoas += 1
    
    match sexo:
        
        case 'M':
            pesoIdeal = (72.7*altura) - 58
        
        case 'F':
            pesoIdeal = (52.1*altura) - 33.7
            
    print(f'O peso ideal de {nome} é {pesoIdeal:.2f}\n')
    
    print(f'Pessoas que participaram: {numPessoas}\n')
    
    try:
        continuar = int(input('Deseja continuar?\nDigite 1 para sim\nDigite 0 para sair!\n'))
    except ValueError or continuar > 1 or continuar < 0:
        pass
    