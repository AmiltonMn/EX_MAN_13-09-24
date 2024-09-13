# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/listamold1.c

def calculoGasolina(precoLitro, valorPgto):
    litros = valorPgto / precoLitro
    return litros
    
nome = input('Digite seu nome\n')
valorLitro = float(input('Digite o valor do litro da gasolina:\n'))
valorPgto = float(input('Digite o valor que você irá colocar de gasolina:\n'))
litrosAbastecidos = calculoGasolina(valorLitro, valorPgto)

print(f'{nome}, você vai abastecer {litrosAbastecidos:.2f} litros de gasolina.')