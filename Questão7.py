# Crie um programa para gerenciar uma lista de tarefas. O programa deve permitir inserir,
# excluir  e marcar tarefas como realizadas. As opções do programa devem ser apresentadas
# através de  um menu (conforme exemplo). Obs.: as ações de inserir, excluir, marcar tarefa
# realizada, listar  tarefas e o menu devem ser feitas através de funções criadas por você. 

lista = []
def inserir():
    tarefa = input("Adicione uma nova tarefa: ")
    print("\n")
    lista.append(tarefa)
    print("Tarefa adcicionada.","\n")
    menu()
    
def marcar():
    c = len(lista)
    x = 0
    i = 1
    print("Escolha uma das tarefas abaixo para marcar como realizada: ","\n")
    while x < c:
      print("Tarefa",i," -> ",lista[x],"\n")
      i += 1
      x += 1
    n = int(input("Digite o número que escolher: "))
    print("\n")
    n -= 1
    lista[n] = lista[n] + "***"
    print("Tarefa marcada.","\n")
    menu()
    
def excluir():
    c = len(lista)
    y = 0
    z = 1
    print("Escolha uma das tarefas abaixo para excluir: ","\n")
    while y < c:
        print("Tarefa",z," -> ",lista[y],"\n")
        y += 1
        z += 1

    n1 = int(input("Digite o número da tarefa que deseja excluir: "))
    print("\n")

    n1 -= 1
    del lista[n1]
    print("Tarefa excluida. ","\n")
    menu()
    
def listar():
    c = len(lista)
    b = 0
    m = 1
    print("Tarefas: ","\n")
    while b < c:
        print(m," --> ",lista[b])
        b += 1
        m += 1
    menu()
    
def sair():
    print("Você saiu do menu")
   
def opção(op):
    if op == 1:
        inserir()
    if op == 2:
        marcar()
    if op == 3:
        excluir()
    if op == 4:
        listar()
    if op == 5:
        sair()
        
def menu():
    print("+","-" * 36,"+","\n"
"|                                      |","\n"
"|       Lista de Tarefas               |","\n"
"|                                      |","\n"
      "+","-" * 36,"+","\n"
"| 1 - Inserir tarefa                   |","\n"
"| 2 - Marcar tarefa como concluida     |","\n"
"| 3 - Excluir tarefas                  |","\n"
"| 4 - Listar tarefas                   |","\n"
"| 5 - Sair                             |","\n"
      "+","-" * 36, "+","\n")

    escolha = int(input("Digite sua opção: "))
    opção(escolha)

menu()
