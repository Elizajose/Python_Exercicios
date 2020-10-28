# Desenvolva um programa que leia 9 (nove) números inteiros e os armazene numa matriz 3x3,
# em seguida mostre na tela os elementos que estão nadiagonal secundária da matriz.

vet = [0]*3
mat = [0]*3
for x in range(3):
    mat[x] = [0]*3
 
for lin in range(3):
    for col in range(3):
        mat[lin][col] = int(input("Informe um número: "))
print("")


 
for lin in range(3):
    for col in range(3):
        
        if lin == col:
            vet[lin] = mat[lin][col]
print(vet)
