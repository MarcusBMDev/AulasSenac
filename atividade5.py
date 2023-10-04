nota1 = float(input ("Insira primeira nota de 0 a 10:"))
nota2 = float(input ("Insira segunda nota de 0 a 10:"))
nota3 = float(input ("Insira terceira nota de 0 a 10:"))
nota4 = float(input ("Insira quarta nota de 0 a 10:"))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
