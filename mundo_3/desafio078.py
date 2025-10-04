numeros = []

for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a Posição {c}: ")))

print("-=" * 30)
print(f"Você digitou os valores {numeros}")

maior = max(numeros)
menor = min(numeros)

print(f"O maior valor digitado foi {maior} nas posições", end=" ")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...", end=" ")

print()
print(f"O menor valor digitado foi {menor} nas posições", end=" ")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...", end=" ")