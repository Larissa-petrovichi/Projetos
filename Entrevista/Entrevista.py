excelente = 0
ruim = 0

    # Entrada de dados do entrevistado

for i in range(50):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Digite a opinião (1-Excelente, 2-Bom, 3-Ruim): "))
    
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

    # Exibir os resultados

print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
