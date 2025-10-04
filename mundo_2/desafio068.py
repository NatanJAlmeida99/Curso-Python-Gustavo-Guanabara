from random import randint

count = 0
victory = 0

while True:
    user = int(input("Digite um valor: "))
    pc = randint(0, 10)
    print(pc)
    tot = user + pc
    option = " "
    while option not in "PI":
        option = str(input("Par ou Ímpar? [P/I]")).strip().upper()
    if option == 'P':
        if tot % 2 == 0:
            print("Você VENCEU")
            victory += 1
        else:
            print("Você PERDEU!")
            break
    elif option == "I":
        if tot % 2 == 1:
            print("Você GANHOU")
            victory += 1
        else:
            print("Você perdeu")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {victory} vezes")