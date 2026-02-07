import os
os.system('cls' if os.name == 'nt' else 'clear')

celsius = [0, 10, 20, 30, 40]

# List Comprehension (Tudo numa linha)
# Lê-se: "Calcula a fórmula PARA cada temp NA lista celsius"
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
