matriz = []

for i in range(3):
    matriz.append([0] * 3)

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()
