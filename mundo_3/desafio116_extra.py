from random import randint
matriz = []
matriz_binaria = []

for i in range(3):
    matriz.append([0] * 3)

for i in range(0, 3):
    matriz_binaria.append([0] * 3)

for i in range(3):
    for j in range(3):
        matriz[i][j] = randint(100, 999)

        if matriz[i][j] % 2 == 0:
            matriz_binaria[i][j] = 0
        else:
            matriz_binaria[i][j] = 1

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()

print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz_binaria[i][j]:^5}]", end="")
    print()