# importa csv
import csv


#CADASTRAR PESSOAS


#IMPRIMIR PESSOAS


#ATUALIZAR PESSOA

nome = input("Digite o nome: ")
for pessoa in pessoas:
    if nome == pessoa['NOME']:
        numero = input("numero: ")
        mail = input("Email: ")
        with open('pessoas.cvs', 'r') as pessoas_cvs:
            leitor = csv.reader(pessoas_csv)
            for linha in linhas:
                if linha == nome:

#DELETAR PESSOA


#menu
while True:
    print("------BIBLIOTECA------")
    print("    1 = PESSOAS       ")
    print("    2 = LIVROS        ")
    print("    3 = EMPRESTIMO    ")
    print("    4 = SAIR          ")
    print("----------------------")
    op = str(input("ESCOLHA UMA OPÇÃO:"))

    if op == "1":
        while True:
            print("------PESSOAS---------")
            print("    1 = CADASTRAR  ")
            print("    2 = IMPRIMIR   ")
            print("    3 = ATUALIZAR  ")
            print("    4 = DELETAR    ")
            print("    5 = ENCERRAR   ")
            print("----------------------")
            op = str(input("ESCOLHA UMA OPÇÃO:"))


            if op == "1":
                print("----CADASTRAR PESSOAS----")

            elif op == "2":
                print("----IMPRIMIR PESSOAS----")



            elif op =="3":
                print("----ATUALIZAR PESSOA----")



            elif op == "4":
                print("----DELETAR PESSOA----")



            elif op == "5":
                break



            else: 
                print("-------------------")
                print("  OPÇÃO INVALIDA   ")
                print("-------------------") 


    elif op == "2":


         while True:
            print("------LIVRO-----------")
            print("    1 = CADASTRAR  ")
            print("    2 = IMPRIMIR   ")
            print("    3 = ATUALIZAR  ")
            print("    4 = DELETAR    ")
            print("    5 = ENCERRAR   ")
            print("----------------------")
            op = str(input("ESCOLHA UMA OPÇÃO:"))


            if op == "1":
                print("----CADASTRAR LIVRO ----")



            elif op == "2":
                print("----IMPRIMIR LIVROS ----")




            elif op =="3":
                print("----ATUALIZAR LIVRO----")



            elif op == "4":
                print("----DELETAR LIVRO ----")



            elif op ==  "5": 
                break    


            else: 



                print("-------------------")
                print("  OPÇÃO INVALIDA   ")
                print("-------------------") 



    elif op =="3":



        while True:
            print("------EMRPESTIMO------")
            print("    1 = CRIAR   ")
            print("    2 = IMPRIMIR    ")
            print("    3 = EMPRESTIMOS ATRASSADO ")
            print("    4 = ATUALIZAR  ")
            print("    5 = DELETAR    ")
            print("    6 = ENCERRAR   ")
            print("----------------------")
            op = str(input("ESCOLHA UMA OPÇÃO:"))


            if op == "1":
                print("----CRIAR EMPRESTIMOS----")



            elif op == "2":
                print("----IMPRIMIR EMPRESTIMOS----")



            elif op == "3":
                print("----EMPRESTIMOS ATRASSADO----")



            elif op == "4":
                print("----ATUALIZAR EMPRESTIMOS----")



            elif op == "5":
                print("----DELETAR PESSOA----")



            elif op == "6":
                break



            else: 
                print("-------------------")
                print("  OPÇÃO INVALIDA   ")
                print("-------------------") 




    elif op == "4":
        break
    else: 
        print("-------------------")
        print("  OPÇÃO INVALIDA   ")
        print("-------------------") 