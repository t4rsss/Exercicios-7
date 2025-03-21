traducao = {
    "casa": "house",
    "gato": "cat",
    "carro": "car",
    "amor": "love",
    "livro": "book"
}

palavra = input("Digite uma palavra em português: ").lower()

if palavra in traducao:
    print(f"A tradução de '{palavra}' é '{traducao[palavra]}'.")
else:
    print("Tradução não encontrada.")
