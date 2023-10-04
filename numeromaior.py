max = None

for i in range(5):
    num = int(input("Digite um número:"))
    if max is None or num > max:
        max = num

print("O número maior é:", max)