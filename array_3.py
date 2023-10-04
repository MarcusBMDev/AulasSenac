vetor1 = []
vetor2 = []
vetor3 = []
for a in range(10):
    num = int(input("Digite um número:"))
    vetor1.append(num)
    if vetor1[a] %2==0:
            vetor2.append(num)
    else:
            vetor3.append(num)
print("Esses são os números digitados pelo user:",vetor1)
print("Esses números são pares:",vetor2)
print("Esses números são impares:",vetor3)




    