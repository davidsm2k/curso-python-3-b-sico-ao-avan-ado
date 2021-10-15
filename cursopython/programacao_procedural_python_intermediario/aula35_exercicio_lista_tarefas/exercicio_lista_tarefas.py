def adicionar_tarefa(tarefa, lista=None):
    if lista is None:
        lista = []
    return lista.append(tarefa)


def desfazer(tarefa, temp=None, lista=None):
    try:
        if lista is None:
            lista = []
        if temp is None:
            temp = []
        temp.append(tarefa)
        return lista.remove(tarefa)
    except Exception as erro:
        print(f'Erro: {erro}')
        return print("Lista vazia")


def refazer(temp=None, lista=None):
    try:
        if lista is None:
            lista = []
        if temp is None:
            temp = []

        if not temp:
            print('Nada a refazer')
            return

        if max(temp) in lista: #Verifica se o item ja foi refeito na lista
            print(f'Item {max(temp)} já foi refeito.')
        else:
            return lista.append(max(temp))
    except Exception as erro:
        print(f'Erro: {erro}')
        return print("Lista vazia")


def exibir_lista(lista):
    if lista == []:
        return print("Lista Vazia")
    else:
        return print(lista)


if __name__ == '__main__':

    lista_tarefas = []
    temp = []

    while True:
        try:
            print("\nMenu de Opções:\n")
            print("1 = Exibir lista\n2 = Adicionar Tarefa\n3 = Desfazer\n4 = Refazer\n5- Sair\n")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                exibir_lista(lista_tarefas)
            if opcao == '2':
                tarefa = input("Digite a terefa que deseja Adicionar: ")
                adicionar_tarefa(tarefa=tarefa, lista=lista_tarefas)
            if opcao == '3':
                desfazer(max(lista_tarefas), temp, lista_tarefas)
            if opcao == '4':
                refazer(temp, lista_tarefas)
            if opcao == '5':
                break
        except Exception as erro:
            print(f'Erro: {erro}')
