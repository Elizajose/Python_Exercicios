# Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode
# ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as
# seguintes opções (todas realizadas através de funções próprias criadas por você):

agenda = {}
def incluirnome():
    numeros = []
    nome = input("Digite um nome para adicionar na agenda: ")
    condi = True
    while condi == True:
        
        numero = int(input("Digite o telefone para adicionar na agenda, ou digite '0' para parar de digitar. "))
        if numero != 0:
            numeros.append(numero)
            agenda[nome] = numeros
        else:
            condi = False
  
    menu()
def incluirtele():
    numeros = []
    nome = input("Digite um nome existente em que deseja incluir um novo telefone: ")
    numero = int(input("Agora digite um novo telefone em que deseja incluir para %s " %(nome) ))
    numeros.append(numero)
    
    if nome in agenda:
        agenda[nome] = agenda[nome] + numeros
    else:
       novonome = nome
       resposta = (input("O nome não existe na agenda. Deseja incluí-lo ? digite 'sim' "))
       
       if resposta == 'sim':
           agenda[novonome] = numeros

    menu()
def excluirtel():
    nome = input("Digite o nome da pessoa em que deseja exlcuir um telefone: ")
    numero = int(input("Agora digite o telefone em que deseja excluir: "))
    
    if len(agenda[nome]) == 1:
        i += len(agenda[nome])
        del agenda[nome]
    else:
        i = 0
    while i < len(agenda[nome]):

        if numero == agenda[nome][i]:
            del agenda[nome][i]

        i += 1
    menu()
def excluirnome():
    nome = input("Digite o nome da pessoa em que deseja deleta-la da agenda: ")
    del agenda[nome]
    
    menu()
def consultar(consulta):
    nome_n = input("Digite o nome da pessoa em que deseja consultar os seus telefones:")
    if nome_n in consulta:
        return str(consulta[nome_n])[1:-1]
    else:
        return print("Nenhum contato encontrado ")
    
    menu()
def menu():
    print("Escolha uma opção: ","\n","A- Incluir novo nome. ","\n",
          "B- Incluir Telefone. ","\n","C- Excluir telefone. ","\n",
          "D- Excluir nome. ","\n","E- Consultar telefone. ")
    n = input("Escolha uma opção: ")
    if n == "A".upper():
        incluirnome()
    if n == "B".upper():
        incluirtele()
    if n == "C".upper():
        excluirtel()
    if n == "D".upper():
        excluirnome()
    if n == "E".upper():
        print("Os telefones são: ",consultar(agenda))

menu()
