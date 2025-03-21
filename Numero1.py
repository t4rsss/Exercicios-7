alunos = {}

while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

print("\nLista de alunos e suas notas:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")
