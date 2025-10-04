times = (
    "Flamengo", "Cruzeiro", "Palmeiras", "Mirassol", "Botafogo","Bahia", "São Paulo", "Fluminense", "RB Bragantino", "Corinthians", "Grêmio", "Ceará", "Vasco", "Internacional", "Santos", "Atlético-MG", "Juventude", "Fortaleza", "Vitória", "Sport"
)

print("-=" * 15)
print(f"Lista de times do Braileirão: {times}")
print("-=" * 15)
print(f"Os 5 primeiros são {times[:5]}")
print("-=" * 15)
print(f"Os 4 últimos são {times[-4:]}")
print("-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 15)
posicao = times.index("Mirassol")
print(f"O Mirassol está na {posicao + 1}° posição")