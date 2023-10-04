def cadastrar_cliente(clientes, nome, telefone, email):
    cliente = {
        'Nome': nome,
        'Telefone':telefone,
        'Email': email
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    print("*****************************")
    print("\n")
def imprimir_cliente(clientes):
    for indice,cliente in enumerate(clientes):
        print(f"ID do cliente {indice+1}")
        print(f"Nome: {cliente['Nome']}")
        print(f"Telefone:{cliente['Telefone']}")
        print(f"Email{cliente['Email']}")
        print("*****************************")
        print("\n")
clientes=[]
nome = input("Digite aqui seu nome:")
telefone = input("Digite aqui seu telefone:")
email = input("Digite aqui seu email:")
cadastrar_cliente(clientes, nome, telefone, email)
imprimir_cliente(clientes)  