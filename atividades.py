 #criando a lista de afazeres
atividades = []

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
    if escolha == "0":
        print("Certo, você saiu da sua lista de afazeres.")  
    if escolha == "1": #se a opção escolhida pela pessoa for = 1, irá inserir tarefa
        print("Você escolheu a opção de inserir tarefas.")   
        tarefa_acrescentada = input("Qual tarefa você deseja acrescentar na lista? ")
        atividades.append(tarefa_acrescentada) #acrescentando tarefas na lista
    if escolha == "2":#se a opção escolhida pela pessoa for = 2, irá listar as tarefas
        print("Aqui está a sua lista de  tarefas: ")  
        print(atividades) #imprimindo a lista 
    if escolha == "3": #se a opção escolhida pela pessoa for = 3, a tarfa será marcada como concluida 
        print("Você escolheu a opção de marcar tarefa como concluida")  
        if escolha == "concluida":
            print ("tarefa concluida")

    if escolha == "4": #se a opção escolhida pela pessoa for = 4, a tarefa será removida da lista
        print("Você escolheu a opção de remover tarefa")
        item_remover = input("Qual ítem você deseja remover? ")
        atividades.remove(item_remover) #removendo ítem da lista
      

