from random import randint

num_random = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print("Os valores sorteado foram:", end=" ")
for c in num_random:
    print(c, end=" ")
print(f"\nO maior valor sorteado foi {max(num_random)}")
print(f"O menor valor sorteado foi {min(num_random)}")