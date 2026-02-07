import os
os.system('cls' if os.name == 'nt' else 'clear')

estudante = 1733


#É usado quando não sabes à partida quantas tentativas vão ser necessárias. 
# A lógica é: "Entra no ciclo e não saias até encontrares o comando break."
while True: 
    # O input é feito sempre aqui
    numero = int(input("Digite o numero de aluno: "))

    if numero == estudante:
        print("Numero de estudante correto.")
        break  # O comando break parte o loop e sai
    
    # Se não entrou no if acima, continua o loop
    print(f"Este não é o teu numero de estudante {numero}!")