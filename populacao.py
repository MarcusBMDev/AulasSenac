A = float(input("Digite o número da população do pais A:"))
B = float(input("Digite o número da população do pais B:"))
taxacres1 = float(input("Digite a taxa de crescimento do Pais A:"))
taxacres2 = float(input("Digite a taxa de crescimento do Pais B:"))
anos = 0
while (A<B):
    A = A*(1+taxacres1/100)
    B = B*(1+taxacres2/100)
    anos = anos+1

print(anos, "ANOS.")
