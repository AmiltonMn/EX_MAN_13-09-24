pres = 0
gov = 0

# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/candidato.c

while pres == 0:
    print('__________________________________________')
    print('________________ ELEICOES ________________')
    print('___ INSIRE O NUMERO DO SEU CANDIDATO A ___')
    print('_______________ PRESIDENCIA ______________')
    print('__________________________________________')

    try:
        if pres != 0:
            pass
        else:
            pres = int(input())
            
            match pres:
                
                case 30:
                    print('José José (Partido Colegista): 30\n\n')
                    
                case 21:
                    print('José Batata (Partido da Batata): 21\n\n')
                    
                case 23:
                    print('Marcos Maionese (Partido da Batata): 23\n\n')
                
                case 41:
                    print('Olavo de Carvalho (Partido da Caveira): 41\n\n')
                    
                case 71:
                    print('Jair de Jair (Partido do Jair): 71\n\n')
                    
                case 11:
                    print('Marcos de Planta (Partido do Herborismo): 11\n\n')
                    
                case 90:
                    print('Lucas de Fogo (Partido do Magma): 11\n\n')
                    
                case 14:
                    print('Ismael de José (Partido do Ismael): 14\n\n')
                    
                case 27:
                    print('Emanoel Gomes (Partido da Caneta Azul): 27\n\n')
                    
                case _:
                    print('Candidato inválido!')
                    pres = 0
    except:
        print('Candidato inválido!')
        pass

    print('__________________________________________')
    print('________________ ELEICOES ________________')
    print('___ INSIRE O NUMERO DO SEU CANDIDATO A ___')
    print('_______________ GOVERNADOR _______________')
    print('__________________________________________')
    
    try:
        if gov != 0:
            pass
        else:
            gov = int(input())
            match gov:
                
                case 12:
                    print('Marcos Pimenta (Partido Pimentinha): 12\n\n')
                    
                case 32:
                    print('Cacilda José (Partido do José): 32\n\n')
                    
                case 41:
                    print('Pedro Fritas (Partido da Batata): 41\n\n')
                
                case 27:
                    print('Emilio Josefino (Partido da Caveira): 27\n\n')
                    
                case 12:
                    print('Neymar (Partido do Futebol): 12\n\n')
                    
                case 5:
                    print('Marcos de Gelo (Partido da água): 5\n\n')
                    
                case 31:
                    print('Carlos Matriz (Partido do XY): 31\n\n')
                    
                case 10:
                    print('Ismael de Geografi (Partido da Pangeia): 10\n\n')
                    
                case 2:
                    print('Lucas Inutilismo (Partido do Rock): 2\n\n')
                    
                case _:
                    print('Candidato inválido!')
                    pres = 0
    except:
        print('Candidato inválido!')
        pass