# Implemente a função splitChars(String) → (Uppercase, Lowercase, Int, Remainder) que recebe
# um argumento String e retorna uma tupla com 4 elementos.

def splitChars(string):
    x = 0
    M = ""
    m = ""
    soma = 0
    r = ""
    while x < len(string):

        if string[x].isupper():
            if string[x] not in M:
                M = M + string[x]  
        elif string[x].islower():
            if string[x] not in m:
                m = m + string[x]
        elif string[x].isdigit():
            i = int(string[x])
            soma = soma + i
        else:
            r = r + string[x]

        x += 1

    return M,m,soma,r

stri = input("Informe algo: ")
result = splitChars(stri)
print(result)
