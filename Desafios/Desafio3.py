# Conceito 3: Estruturas de Controle - Laços de Repetição

soma_pares = 0

for i in range(1, 21):
    if i % 2 == 1:
        print(f"{i} - Impar")    
    else:
        print(f"{i} - Par")
        soma_pares += i

print(f"Soma total dos pares é: {soma_pares}")