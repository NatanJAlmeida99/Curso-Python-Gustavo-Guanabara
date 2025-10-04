from random import randint

pc = randint(0, 10)
correct = False
trys = 0
print("Acabei de pensar em um número entre 0 e 10")
print("Será que você consegue adivinhar qual foi? ")
print(pc)

while not correct:
    user = int(input("Qual é seu palpite? "))
    trys += 1
    if user == pc:
        correct = True
    else:
        if user < pc:
            print("Mais... Tente mais uma vez")
        elif user > pc :
            print("Menos... Tente mais uma vez")

print(f"Acertou com {trys} tentativas. Parabéns!")