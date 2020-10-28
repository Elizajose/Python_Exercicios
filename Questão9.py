# Escreva um programa que lê duas notas de vários alunos e armazena estas notas em um dicionário,
# onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string
# vazia como nome. Escreva uma função que permita retornar a média do aluno, dado o seu nome
# como argumento.

dic={}
n1=0
n2=0
nome="Perder para a razão, sempre é ganhar"
while nome!="":
    nome = input("Digite o seu nome: ")
    if nome!="":    
        n1 = float(input("Digite a sua primeira  nota: "))
        n2 = float(input("Digite a sua segunda  nota: "))
        dic[nome] = [n1,n2]

def média (nome):
    n1=dic[nome][0]
    n2=dic[nome][1]
    m=(n1+n2)/2
    return m
a=input("Digite o nome do aluno para saber sua média: ")
m=média(a)
print("A média do aluno",a,"é",m)
