def verificar_nota(valor):
    if valor >= 10:
        return "Aprovado"
    else:
        return "Reprovado"

# Agora basta chamar a função
resultado = verificar_nota(16)
print(resultado)