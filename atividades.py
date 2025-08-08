#criando a lista de afazeres
atividades = []

with  open ("banco_de_dados.txt", "r") as arquivo: #abrindo o arquivo em txt
            for tarefa in atividades:
                atividades.append(tarefa.strip())


while True:
    #criando o menu
    print("""
        ***************************************************
        * SEJA BEM VINDO (A) A SUA LISTA DE AFAZERES!!!!  *
        *      Qual das opções a seguir você gostaria?    *
        *      1- Inserir tarefas                         *
        *      2- Listar tarefas                          *
        *      3- Marcar como concluido                   *
        *      4- Remover tarefa                          *
        *      0- Sair                                    *
        *************************************************** """)


    escolha = input("Qual opção da lista acima você deseja? ")

    if escolha == "1": #se a opção escolhida pela pessoa for = 1, irá inserir tarefa
        print("Você escolheu a opção de inserir tarefas.")   
        tarefa_acrescentada = input("Qual tarefa você deseja acrescentar na lista? ")
        atividades.append(tarefa_acrescentada) #acrescentando tarefas na lista

    if escolha == "2":#se a opção escolhida pela pessoa for = 2, irá listar as tarefas
        cont = 0 
        for tarefa in atividades:
            print(f"{cont} - {tarefa}")
            cont += 1

    if escolha == "3": #se a opção escolhida pela pessoa for = 3, a tarfa será marcada como concluida 
        cont = 0 
        for tarefa in atividades:
            print(f"{cont} - {tarefa}")
            cont += 1
        tarefa_concluida =  int(input("Qual tarefa você deseja concluir? (escolha por número) "))
        atividades[tarefa_concluida] = atividades[tarefa_concluida] + "(X)"
       
    if escolha == "4": #se a opção escolhida pela pessoa for = 4, a tarefa será removida da lista
        print("Você escolheu a opção de remover tarefa")
        item_remover = int(input("Qual ítem você deseja remover? (escolha plo numero da tarefa) "))
        atividades.pop(item_remover) #removendo ítem da lista

    if escolha == "0":
        print("Certo, você saiu da sua lista de afazeres.")  
        with  open ("banco_de_dados.txt", "w") as arquivo: #abrindo o arquivo em txt
            for tarefa in atividades:
                arquivo.write(tarefa + "\n") #escrevendo a tarefa
        print("Lista de tarefas salva com sucesso! ")

     
        break

    
      

