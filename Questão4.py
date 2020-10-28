# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprime a data
# com o nome do mês por extenso.

data=input("Informe sua data de nascimento: ")
dia=[0,1,2,3,4,5,6,7,8,9]
ano=[]
nome=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
mes= (int)(data[3:5])
dia=(data[0:2])
ano=(data[6:])
print("Você nasceu em ",dia,"de ",nome[mes-1], "de ",ano,".")
