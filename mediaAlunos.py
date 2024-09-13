# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listacondicional6.c

try:
    qtdAlunos = int(input('De quantos alunos você quer fazer a média?\n'))
    qtdNotas = int(input('Qual a quantidade de notas?\n'))
except :
    pass

mediaAlunos = []
aprovado = ''
media = 0

for i in range(qtdAlunos):
    matricula = input(f'Qual a matrícula do {i + 1}° aluno?\n')
    
    for j in range(qtdNotas):
        nota = int(input(f'Digite a {j + 1}° nota do aluno de matrícula {matricula}:\n'))
        media += nota
        
    media = media/qtdNotas
    
    if media >= 9:
        conceito = 'A'
        aprovado = 'APROVADO'
    elif media >= 7.5:
        conceito = 'B'
        aprovado = 'APROVADO'
    elif media >= 6:
        conceito = 'C'
        aprovado = 'APROVADO'
    elif media >= 4:
        conceito = 'D'
        aprovado = 'REPROVADO'
    elif media < 4:
        conceito = 'E'
        aprovado = 'REPROVADO'
        
    resultado = f'O aluno de matricula {matricula} teve média {conceito}({media}) e foi {aprovado}'
    
    mediaAlunos.append(resultado)


for i in range(len(mediaAlunos)):
    print(mediaAlunos[i])