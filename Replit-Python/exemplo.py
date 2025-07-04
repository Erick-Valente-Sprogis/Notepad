    # Define o salário
salario = int(input("Qual o valor do seu salário? "))

    # Inicializa a variável para acumular o total das contas
total_contas = 0

    # Pergunta ao usuário quantas contas ele deseja informar
quantidade_de_contas = int(input("Quantas contas você deseja informar? "))

    # Loop para coletar os valores das contas
for i in range(quantidade_de_contas):
    conta = float(input(f"Digite o valor da conta {i+1}: "))
    total_contas += conta

    # Calcula o valor restante após pagar todas as contas
valor_restante = salario - total_contas

    
print(f"Total das contas: R${total_contas:.2f}")
print(f"Saldo: R${valor_restante:.2f}")
print("END")



import csv

with open('exemplo.csv', newline='')as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)