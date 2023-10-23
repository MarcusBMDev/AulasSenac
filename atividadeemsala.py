from datetime import datetime   #Chama de biblioteca
import csv #Chamada de biblioteca

tarefas = [] #Definindo o Array

def criar_tarefa(tarefas):
    tarefa = {
        'Nome': input("Digite o nome da tarefa: "),
        'Tipo': input("Insira o tipo de tarefa: "),
        'Observacao': input("Informe a observação da tarefa:"),
        'Data de entrega': input("Insira a data da tarefa: AAAA-MM-DD "),
    }

    tarefas.append(tarefa)
    criar_csv()
    print("")
    print("Tarefa cadastrada com sucesso!")
    print("")

def criar_csv():
    gravador = csv.writer(open('arquivo_tarefa.csv', mode="w", newline='')) 
    gravador.writerow(["Nome","Tipo","Observacao","Data de entrega"])

    for tarefa in tarefas:
            nome = tarefa['Nome']
            tipo = tarefa['Tipo']
            observacao = tarefa['Observacao']
            data_de_entrega = tarefa['Data de entrega']
            gravador.writerow([tarefa['Nome'],tarefa['Tipo'],tarefa['Observacao'],tarefa['Data de entrega']])



#Menu
while True:
    print("Bem-vinde!")
    print("Escolha um:")
    print("1 - Cadastra tarefa")
    print("2 - Ler CSV")
    print("3 - Atualizar informações da tarefa")
    print("4 - Excluir")
   
    opc = int(input(""))
    print("")
    
    if opc == 1:
        criar_tarefa(tarefas)
    


#def atualizar_tarefa(tarefas):
    pesquisa = input("Digite o nome que deseja atualizar: ")
    for tarefa in tarefas:
        if tarefa['Nome'] == pesquisa:
            tarefa['Nome'] = input("Digite o nome do produto: ")
            tarefa['Valor'] = input("Insira o valor do produto: ")
            tarefa['Quant'] = input("Informe a quantidade:")
            tarefa['Frete'] = input("Insira o valor do frete: ")