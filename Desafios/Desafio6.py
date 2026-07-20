#conceito 6 - Dicionários

produto = {
    "nome": "Camiseta",
    "preco": 29.90,
    "estoque": 155
}

print(f"O produto {produto['nome']} custa R${produto['preco']} e possui {produto['estoque']} unidades em estoque.")

produto["estoque"] = produto["estoque"] + 10
produto["preco"] = produto["preco"] * 0.95

def resumo_produto(produto):
    return f"{produto['nome']} - R${produto['preco']:.2f} - {produto['estoque']} unidades"

print(resumo_produto(produto))