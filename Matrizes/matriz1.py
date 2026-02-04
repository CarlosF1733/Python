import os
os.system('cls' if os.name == 'nt' else 'clear')

imagem = [
    [0, 128, 255],
    [50, 200, 50],
    [255, 128, 0]
]

for linha in imagem:       # A variavel 'linha' vai ser [0, 128, 255] na 1ª volta
    for pixel in linha:    # A variavel 'pixel' vai ser 0, depois 128...
        print(pixel, end=" ") # O end=" " evita o \n automático
    print() # Muda de linha no fim da linha atual