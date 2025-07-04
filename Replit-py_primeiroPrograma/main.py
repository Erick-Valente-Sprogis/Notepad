#Cálculo de Média

nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
    print(media)
elif media >= 5:
    print("Aprovado Primeira Parte\n")
    print(media)
    print("Recuperação")
else:
    print("Reprovado")
    print(media)

print("END")
