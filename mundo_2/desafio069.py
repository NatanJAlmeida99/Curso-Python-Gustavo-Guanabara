tot18 = toth = tot20 = 0

while True:
    age = int(input("Idade: "))
    sex = " "
    while sex not in "MF":
        sex = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    
    if sex == "M":
        toth += 1
    
    if sex == "F" and age < 20:
        tot20 += 1
    
    option = " "
    while option not in "SN":
        option = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if option == "N":
        break

print(f"O total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {toth} homens cadastrados")
print(f"E temos {tot20} mulheres com menos de 20 anos")