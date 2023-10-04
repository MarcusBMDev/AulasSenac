alunos = ["Marcus", "Isis", "Hugo", "Luan", "Igor"]
notas = []
medias = []
soma = 0
cont = 0

for i in range(5):
    for a in range(4):
        nota = float(input(f"Digite as 4 notas do {alunos[i]}:"))
        soma = soma + nota
        media = soma / 4
    if media >= 7:
            cont = cont + 1
    soma = 0
    medias.append(media)
        

print("A média dos alunos são:", medias)
print("Número de alunos aprovado >=7:", cont )
    
    
