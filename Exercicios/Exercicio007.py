aluno = str(input("Digite o nome do aluno: "))
nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

print("A primeira nota do aluno {} eh {} e a segunda {} e a sua media eh {}"
      .format(aluno, nota1, nota2, media))