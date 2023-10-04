nota = [5,2,1,0]
media = 0
for i in range(len(nota)):
    media = media + nota [i]/4
if  media <=7:
    print(nota, media,"REPROVADO")
else:
    print(nota, media,"APROVADO")