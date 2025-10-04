matriz = []
totPar = totTerceira = maiorSegunda = 0

for i in range(3): # Números de linhas
    matriz.append([0] * 3) # Número de colunas

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
        if matriz[i][j] % 2 == 0:
            totPar += matriz[i][j]
        if j == 2:
            totTerceira += matriz[i][j]
        if i == 1:
            maiorSegunda = matriz[i][j]
            if matriz[i][j] > maiorSegunda:
                maiorSegunda = matriz[i][j]

print("-=" * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()
print("-=" * 30)

print(f"A soma dos valores pares {totPar}")
print(f"A sina dos valores da terceira coluna é {totTerceira}")
print(f"O maior valor da segunda linha é {maiorSegunda}")
