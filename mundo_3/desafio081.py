numeros = []
count = 0

while True:
    num = int(input("Digite um valor: "))
    numeros.append(num)
    count += 1

    resp = " "
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break

numeros.sort(reverse=True)

print("=-" * 30)
print(f"Você digitou {count} elementos. ")
print(f"Os valores em ordem decresente são {numeros}")

if 5 in numeros:
    print("O valor 5 faz parte da lista! E está nas posições: ", end=" ")
    for i, v in enumerate(numeros):
        if v == 5:
            print(f"{i}...", end=" ")
else:
    print("O valor 5 não faz parte da lista")