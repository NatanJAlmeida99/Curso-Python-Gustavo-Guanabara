# Minha forma de resolver

"""from datetime import datetime

dados = {}
year_atual = datetime.now().year

nome = str(input("Nome: "))
year_born = (int(input("Ano de Nascimento: ")))
ctps = int(input("Carteira de Trabalho (0 não tem): "))
age = year_atual - year_born

dados["Nome"] = nome
dados["Idade"] = age
dados["CTPS"] = ctps

if ctps == 0:
    print("-=" * 30)
    for k, v in dados.items():
        print(f" - {k} tem o valor {v}")
else:
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salário"] = float(input("Salário: R$"))
    aposentadoria = dados["Contratação"] + 35
    age_aposentadoria = aposentadoria - year_born
    dados["Aposentadoria"] = age_aposentadoria

    for k, v in dados.items():
        print(f" - {k} tem o valor {v}")"""

# Forma de resolver professor Gustavo Guanabra
from datetime import datetime
dados = dict()
dados["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - nasc
dados["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))
if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: R$"))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"]) + 35) - datetime.now().year
print("-=" * 30)
for k, v in dados.items():
    print(f" - {k} tem o valor de {v}")