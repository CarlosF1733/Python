import os
os.system('cls' if os.name == 'nt' else 'clear')

def conversor(dolar):
    euro = 1.10 * dolar
    return euro

dolar = float(input("Quantos dolares tens? "))

resultado = conversor(dolar)

print(f"Tu tens {resultado:.2f} euros")