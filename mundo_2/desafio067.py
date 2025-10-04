while True:
    num = int(input("Quer ver a tabuaba de qual valor? "))
    print("-" * 20)
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(f"{num} x {c} = {num * c}")
    print("-" * 20)
print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!")