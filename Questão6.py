# Crie uma função que calcula e retorna a média de uma lista de números de ponto flutuante.
# Agora faça um programa que recebe a temperatura média de cada um dos meses do ano e  armazene-as
# em uma lista. Em seguida, com o auxílio da função criada por você obtenha e mostre  todas as
# temperaturas acima da média anual, e em que meses elas ocorreram (mostrar o nome  do mês por
# extenso: 1 – Janeiro, 2 – Fevereiro, . . ., 12 – Dezembro). 

mês = {1: 'janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro',10: 'Outubro',11: 'Novembro', 12: 'Dezembro'}
l = []
a = 0
m = float(0.0)
for i in range (0,12):
    a = float(input("Digite a temperatura de %s - %s (ºC): " %(str(i+1),mês[i+1])))
    l.append(a)    

def somAnual(v1):
    s= 0.0
    for c in range(12):
        s=s+v1[c]  
    return float(s)

m=somAnual(l)/12


for i in range (12):
    
    if l[i] > m:
        print('A temperatura',l[i],'ºC referente ao mês',i+1,' - ',mês[i+1], 'está acima da média anual')
