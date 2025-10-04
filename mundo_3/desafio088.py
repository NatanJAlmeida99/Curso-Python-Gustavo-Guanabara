from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print("         Joga na MEGA SENA           ")
print('-' * 30)
qtnd = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1

while tot <= qtnd:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print("-=" * 3, f" SORTEANDO {qtnd} JOGOS", "-=" * 3)

for i, l in enumerate(jogos):
    print(f"Jogo {i + 1}: {l}")
    sleep(1)
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)