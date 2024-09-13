# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/Imposto%20de%20Renda.c

continuar = 1

while continuar == 1:
    nome = str(input('Digite o nome do funcionário:\n'))
    numDep = int(input('Digite o número de dependentes:\n'))
    salarioLiquido = 0
    somaINSS = 0
    salIR = 0
    somaIR = 0

    for i in range(12):
        salarioBruto = float(input(f'Digite o {i + 1}° salário bruto\n'))
        
        if salarioBruto <= 1412.00:
            valorINSS = salarioBruto * 0.075
            somaINSS += valorINSS
            salarioLiquido = salarioBruto - valorINSS
            
        elif salarioBruto <= 2666.69:
            valorINSS = salarioBruto * 0.09
            somaINSS += valorINSS
            salarioLiquido = salarioBruto - valorINSS
            
        elif salarioBruto <= 4000.03:
            valorINSS = salarioBruto * 0.12
            somaINSS += valorINSS
            salarioLiquido = salarioBruto - valorINSS
        
        else:
            valorINSS = salarioBruto * 0.14
            somaINSS += valorINSS
            salarioLiquido = salarioBruto - valorINSS
            
        if numDep > 0:
            salIR = salarioLiquido - (numDep * 189.59)
            
            if salIR <= 1903.98:
                valorIR = 0
                somaIR += valorIR

            elif salIR <= 2826.65:
                valorIR = ((salIR * 0.075) - 142.80)
                somaIR += valorIR
                
            elif salIR <= 3751.05:
                    valorIR = ((salIR * 0.15) - 354.80)
                    somaIR += valorIR

            elif salIR <= 4664.68:
                    valorIR = ((salIR * 0.225) - 636.13)
                    somaIR += valorIR
                    
            else:
                valorIR = ((salIR * 0.275) - 869.36)
                somaIR += valorIR
        
        else:
            salIR = salarioLiquido
            
            if salIR <= 1903.98:
                valorIR = 0
                somaIR += valorIR

            elif salIR <= 2826.65:
                valorIR = ((salIR * 0.075) - 142.80)
                somaIR += valorIR
                
            elif salIR <= 3751.05:
                    valorIR = ((salIR * 0.15) - 354.80)
                    somaIR += valorIR

            elif salIR <= 4664.68:
                    valorIR = ((salIR * 0.225) - 636.13)
                    somaIR += valorIR
                    
            else:
                valorIR = ((salIR * 0.275) - 869.36)
                somaIR += valorIR
        
        salarioLiquido -= valorIR
        print(f'Salario liquido = {salarioLiquido:.2f}')
        print(f'Valor INSS = {valorINSS:.2f}')
        print(f'Valor IR = {valorIR:.2f}')
            
    print(f'Funcionário: {nome}')
    print(f'Valor no ano a pagar de INSS = {somaINSS:.2f}')
    print(f'Valor no ano a pagar IR = {somaIR:.2f}')

    continuar = int(input('Para visualizar o IR de outro funcionário, digite 1, para sair digite 0\n'))
        