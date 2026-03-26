alunos = int(input("Quantos alunos deseja cadastrar: "))
notas = int(input("Quantas notas serão cadastradas: "))

for i in range(alunos):
    nome = input(f"\nNome do aluno {i+1}: ")
    lista = [float(input(f"Nota {j+1}: ")) for j in range(notas)]
    media = sum(lista)/notas
    if media >= 6: sit = "Aprovado"
    elif media < 4: sit = "Reprovado"
    else: sit = "Recuperação"
    print(f"{nome} - Notas: {lista} - Média: {media:.2f} - {sit}")