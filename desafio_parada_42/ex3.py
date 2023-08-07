"""

3) Faça um programa no qual o usuário precisa cadastrar as informações de um
produto: código, nome, quantidade e preço. No final o programa deve
mostrar as informações cadastradas e exibir o valor total da compra.

"""
produtos = []
total = 0
valor_total_compra = 0
while True:
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço unitário do produto: "))

    produtos.append((codigo,nome,quantidade,preco))

    print("\n==== Produtos Cadastrados ====")
    for codigo, nome, quantidade, preco in produtos:
        total = quantidade * preco
        print(f"Código: {codigo}, Nome: {nome}, Quantidade: {quantidade}, Preço: R${preco:.2f}, Valor total: R${total:.2f}")

    valor_total_compra += quantidade * preco
    print(f"\nValor total da compra: R${valor_total_compra:.2f}")

    continuar = input("Deseja cadastrar mais um produto? (S/N): ").upper()
    if continuar != "S":
        break

print(f"\nValor total da compra: R${valor_total_compra:.2f}")