def area(width, height):
    print(f"A área de um terrono {width} x {height} é de {width * height}m²")


print(" Controle de Terrnos")
print("-" * 30)
w = float(input("LARGURA (m): "))
h = float(input("COMPRIMENTO (m): "))
area(w, h)