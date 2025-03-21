catalogo = {
    1: ("banana", 2.00),
    2: ("uva", 8.00),
    3: ("pera", 5.00),
    4: ("melancia", 15.00),
    5: ("abobora", 20.00)
}

codigo = int(input("Digite o código do produto: "))

if codigo in catalogo:
    nome, preco = catalogo[codigo]
    print(f"Produto: {nome}, Preço: R$ {preco:.2f}")
else:
    print("Código não encontrado.")
