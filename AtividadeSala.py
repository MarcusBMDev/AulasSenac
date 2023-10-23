def deleter_livro(livros_csv, pesquisa):
    livros_para_remover = []

    with open(livros_csv, 'r') as file:
        reader = csv.DictReader(file)
        livros = list(reader)

    for livro in livros:
        if livro['TITULO'] == pesquisa:
            livros_para_remover.append(livro)

    if not livros_para_remover:
        print("Nome não encontrado no arquivo CSV!")
    else:
        with open(livros_csv, 'w', newline='') as file:
            fieldnames = ['TITULO'] 
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for livro in livros_para_remover:
                livros.remove(livro)  # Remove da lista
                # Não escreve o livro removido de volta no arquivo CSV

            writer.writerows(livros)  # Escreve o restante de volta no arquivo CSV

        print("Livro(s) removido(s) com sucesso do arquivo CSV e da lista!")

#DELETAR PESSOA		
def deleter_pessoa(pessoas_csv, pessoas):
    pesquisa = input("Digite o nome que deseja excluir: ")
    pessoas_para_remover = []

    # Encontra o índice das pessoas a serem removidas na lista
    for i, pessoa in enumerate(pessoas):
        if pessoa['NOME'] == pesquisa:
            pessoas_para_remover.append(i)

    if not pessoas_para_remover:
        print("Nome não encontrado na lista!")
    else:
        # Abre o arquivo CSV para leitura e escrita
        with open(pessoas_csv, 'r') as file:
            reader = csv.DictReader(file)
            pessoas_no_arquivo = list(reader)

        # Remove as pessoas da lista em memória
        for i in reversed(pessoas_para_remover):
            pessoas.remove(i)

        # Abre o arquivo CSV para escrita e escreve as pessoas restantes
        with open(arquivo_pessoas_csv, 'w', newline='') as file:
            fieldnames = pessoas_no_arquivo[0].keys()  # Obtém os cabeçalhos do CSV do arquivo
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(pessoas_no_arquivo)  # Escreve as pessoas restantes

        print("Pessoa(s) removida(s) com sucesso do arquivo CSV e da lista!")





def deleter_registro(emprestimos):
	pesquisa = input("Digite o nome que deseja excluir: ")
    for emprestimo in emprestimos:
        if emprestimo['EMPRESTIMO'] == pesquisa:
            emprestimos.remove(emprestimo)
        else:
            print("Nome não encontrado na lista!")            
    criar_csv()