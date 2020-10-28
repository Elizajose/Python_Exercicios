# Faça um programa que leia 2 (duas) strings e em seguida informa o conteúdo delas seguido do
# seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e se são
# iguais ou diferentes no conteúdo.

string1 = input('String 1: ')
string2 = input('String 2: ')

print('Tamanho de "%s": %d caracteres' % (string1, len(string1)))
print('Tamanho de "%s": %d caracteres' % (string2, len(string2)))

if (len(string1) != len(string2)):
    print("As duas strings sao de tamanhos diferentes")
    print("As duas strings possuem conteudo diferente")
else:
    print("As duas strings tem tamanho igual")
    if (string1 == string2):
        print("As duas strings possuem o mesmo conteudo")
    else:
        print("As duas strings possuem conteúdo diferente")
    
