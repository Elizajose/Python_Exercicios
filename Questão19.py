# Implemente uma função chamada eliminarRepetidos([ Int ]) → [ Int ], que recebe uma lista de
# inteiros e devolve a mesma lista, mas sem elementos repetidos, mantendo apenas a primeira
# ocorrência de cada elemento.

def eliminarepetidos(l):
    i = 0
    z = 1
    cont = 0
    while i < len(l):
        x = z
        while x < len(l):
            
            if l[i] == l[x]:
                l[x] = []
            x += 1
        z += 1
        i += 1
        
    tr = True
    
    while tr == True:
        i = 0
        while i < len(l):
            
            if l[i] == []:
                del l[i]
                
            i += 1
            
        if [] in l:
            tr = True
        else:
            tr = False
            
    return l
    
              
num = [1,2,3,4,5,6,7,1,2,3,4,9,9,0]
print(eliminarepetidos(num))
