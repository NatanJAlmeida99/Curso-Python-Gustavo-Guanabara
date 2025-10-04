from time import sleep

def maior(*numeros):
    print("Analisando valores informados...")
    sleep(1)
    maior = None  # começa vazio
    for valor in numeros:
        print(f"{valor} ", end=" ", flush=True)
        sleep(0.5)
        if (maior is None) or (valor > maior):
            maior = valor
    print(f"\nForam informados {len(numeros)} valores ao todo.")
    print(f"O maior valor informado foi {maior}")
        
maior(2, 9, 4, 5, 7, 1)
maior(10)