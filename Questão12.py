# Implemente uma função que, dado um número n maior que 2,devolve uma String com todos os
# números primos menores ou iguais a n, separados por espaços em branco.

def primo(numero):
    primo = True

    if(numero == 1):
        return False

    for i in range(2,numero):
        if(numero%i == 0):
            primo = False

    if (primo == True):
        return True
    else:
        return False


n = int(input("Informe um número: "))


for i in range(2,n):
    if(primo(i)):
       
        print(str(i),end=" ")
       
   


