while True:
    nota = float(input("Digite uma nota entre 0 e 10:"))
    if nota >= 0 and nota <= 10:
        print("Nota valida", nota)
        break
    else:
        print("Nota inválida. Digite novamente!")
    