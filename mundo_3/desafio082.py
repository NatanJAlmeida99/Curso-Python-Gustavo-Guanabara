numeros = []
isPar = []
isImpar = []

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        isPar.append(num)
    else:
        isImpar.append(num)
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == 'N':
        break

print("-=" * 40)
print(f"A lista completa é {numeros}")
print(f"A lista pares é {isPar}")
print(f"A lista ímpares é {isImpar}")