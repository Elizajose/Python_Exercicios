# Crie um programa que solicite o nome do usuário e o imprima no formato de escada.


nome = str(input("Informe um nome: ")).upper()
for i in range(0, len(nome)+1):
    print(nome[:i])


