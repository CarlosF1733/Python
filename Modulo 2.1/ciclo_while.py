import os
os.system('cls' if os.name == 'nt' else 'clear')

pressao_atual = 2
setpoint = 5

while pressao_atual < setpoint:
    print(f"Pressão em {pressao_atual} bar... Bomba ligada!")
    pressao_atual += 1  # Aumentamos a pressão a cada volta

print("Pressão atingida. Bomba desligada.")