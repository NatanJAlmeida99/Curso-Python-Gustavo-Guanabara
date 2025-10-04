print("=" * 30)
print("10 TERMOS DE UMA PA".center(30))
print("=" * 30)

first = int(input("Primeiro termo: "))
jump = int(input("Razão: "))
termo = first
cont = 1

while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += jump
    cont += 1
print("FIM")