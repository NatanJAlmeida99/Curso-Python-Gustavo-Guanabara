count = 1

num = int(input("Digite um número: "))
next = str(input("Quer continuar? [S/N] ")).strip().upper()
sum = num
menor = num
maior = num

while next not in "N":
    num = int(input("Digite um número: "))
    sum += num
    next = str(input("Quer continuar? [S/N] ")).strip().upper()
    count += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Você digitou {count} números e a média foi {sum / count}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
    