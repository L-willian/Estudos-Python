alunos = ["Luiz", "Maria", "João", "Ana", "Pedro"]

alunos.append("Clara")

print(alunos[0])
print(alunos[-1])

for index, aluno in enumerate(alunos):
    print(f"{index}: {aluno}")

alunos.pop(1)

print("Após remover o segundo aluno:")

for index, aluno in enumerate(alunos):
    print(f"{index}: {aluno}")
