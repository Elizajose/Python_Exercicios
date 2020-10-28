nomeAtleta = ' '

while (nomeAtleta != ''):
    nomeAtleta =input('Atleta: ')

    if (nomeAtleta != ''):
        primeiroVolta = float(input('Primeiro Volta: '))
        segundoVolta = float(input('Segundo Volta: '))
        terceiroVolta = float(input('Terceiro Volta: '))
        

        somaVoltas = primeiroVolta + segundoVolta + \
            terceiroVolta
        if (primeiroVolta >= segundoVolta) and \
           (primeiroVolta >= terceiroVolta):
            melhorVolta = primeiroVolta
            
        elif (segundoVolta >= terceiroVolta) and \
             (terceiroVolta >= primeiroVolta):
            melhorVolta = segundoVolta
            
        elif (terceiroVolta >= primeiroVolta) and \
             (terceiroVolta >= segundoVolta):
            melhorVolta = terceiroVolta
        else:
            print("")
        
       

        if (primeiroVolta <= segundoVolta) and \
           (primeiroVolta <= terceiroVolta):
            piorVolta = primeiroVolta
        elif (segundoVolta <= terceiroVolta) and \
             (terceiroVolta <= primeiroVolta):
            piorVolta = segundoVolta
        else:
            print("")
            
        

        print('Melhor volta: %.2f m' % (melhorVolta))
        print('Pior Volta: %.2f m' % (piorVolta))
        print('Media das demais voltas: %.2f m' % (somaVoltas / 3.0))

        print('Resultado Final: ')
        print('%s: %.2f m' % (nomeAtleta, (somaVoltas / 3.0)))
