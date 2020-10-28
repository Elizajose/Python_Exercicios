# Crie a função busca(String, [String]) → [String] que recebe uma String e uma lista de Strings
# e retorna todas as Strings da lista que começam com a String passada como parâmetro.

def busca(st,stl):
    x = 0
    encontradas = []
    while x < len(stl):
        
        c = 0
        cont = 0
        
        while c < len(stl[x]) and c < len(st):
            
            if st[c] == stl[x][c]:
                cont += 1
                
            c += 1
            
        if cont == len(st):
            encontradas.append(stl[x])

        x += 1
        
    return encontradas

st = input("Informe algo: ")
lista = ["Samba", "Maracatu Rural", "Frevo", "Maraca", "Maracatu Nação", "Maravilha", "Cavalo Marinho", "Maracatus"]
encontradas = busca(st,lista)
print(encontradas)
