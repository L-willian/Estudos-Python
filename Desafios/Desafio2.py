# Conceito 2: Estruturas de Controle e indentação

idade = 18

if idade < 12:
    faixa = "Criança"
elif idade >= 12 and idade <= 17:
    faixa = "Adolescente"
elif idade >= 18 and idade <= 59:
    faixa = "Adulto"
else:
    faixa = "Idoso"


print(f"A faixa étaria é: {faixa}")

status = "Pode Dirigir" if idade >= 18 else "Não pode Dirigir"

print(f"{status}")