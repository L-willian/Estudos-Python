# Conceito 7: Tratamento de Exceções

def dividir_seguro(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return None
    

def buscar_valor_dict(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        print(f"Erro: A chave '{chave}' não foi encontrada no dicionário.")
        return None
    
a = 10
b = 0
resultado_divisao = dividir_seguro(a, b)
if resultado_divisao is not None:
    print(f"O resultado da divisão é: {resultado_divisao}")

meu_dict = {'nome': 'Alice', 'idade': 30}
chave = 'cidade'
valor = buscar_valor_dict(meu_dict, chave)
if valor is not None:
    print(f"O valor associado à chave '{chave}' é: {valor}")

