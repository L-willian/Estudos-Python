# Conceito 5 - Funções 

def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade >= 12 and idade <= 17:
        return "Adolescente"
    elif idade >= 18 and idade <= 59:
        return "Adulto"
    else:
        return "Idoso"
        
def media(lista_notas):
    return sum(lista_notas) / len(lista_notas)


idade = 20
faixa_etaria = classificar_idade(idade)
print(f"A pessoa está na faixa etária: {faixa_etaria}")

lista_notas = [1, 2, 4, 7]

media_notas = media(lista_notas)
print(f"A média das notas é: {media_notas}")