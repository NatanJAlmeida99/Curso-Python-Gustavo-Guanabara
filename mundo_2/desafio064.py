num = 0
count = 0
sum = 0

num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    sum += num
    count += 1
    num = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {count} e a soma entre eles foi {sum}")