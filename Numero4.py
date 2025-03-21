frase = input("Digite uma frase: ").lower()
palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print("\nContagem de palavras:")
print(contagem)
