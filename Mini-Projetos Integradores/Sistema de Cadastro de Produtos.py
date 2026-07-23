# Sistema de Cadastro de Produto

estoque = []

def cadastrar_produto(estoque,nome, preco, quantidade):
    produto =  {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    try:
        if not isinstance(preco, (int, float)) or not isinstance(quantidade, (int, float)):
            raise TypeError("Preço e quantidade devem ser números.")
    except TypeError:
        print("Erro: Preço e quantidade devem ser números.")
        return  
    try:
        if preco < 0 or quantidade < 0:
            raise ValueError("Preço e quantidade devem ser valores positivos.")
    except ValueError as e:
        print(f"Erro: {e}")
        return
    estoque.append(produto)

def listar_produtos(estoque):
    print("Estoque de produtos:")
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for produto in estoque:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def buscar_produto(estoque, nome):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

def remover_produto(estoque, nome):
    produto = buscar_produto(estoque, nome)
    if produto:
        estoque.remove(produto)
        return True
    return False



while True:
    print("\nMenu:")
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Buscar produto")
    print("4 - Remover produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        cadastrar_produto(estoque, nome, preco, quantidade)
    elif opcao == "2":
        listar_produtos(estoque)
    elif opcao == "3":
        nome = input("Digite o nome do produto que deseja buscar: ")
        produto = buscar_produto(estoque, nome)
        if produto:
            print(f"Produto encontrado: Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
        else:
            print(f"Produto '{nome}' não encontrado.")
    elif opcao == "4":
        nome = input("Digite o nome do produto que deseja remover: ")
        if remover_produto(estoque, nome):
            print(f"Produto '{nome}' removido com sucesso.")
        else:
            print(f"Produto '{nome}' não encontrado.")
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
