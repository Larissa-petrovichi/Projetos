# Entrada de dados
valor_total = float(input("Digite o valor total da compra: R$ "))

# Verificação de desconto
if valor_total < 200:
    print("Você ganhou um desconto de 5%")
    desconto = valor_total * 0.05

elif valor_total >= 200 and valor_total < 300:
    print("Você ganhou um desconto de 10%")
    desconto = valor_total * 0.10

else:
    print("Você ganhou um desconto de 15%")
    desconto = valor_total * 0.15

# Cálculo do valor final
valor_a_pagar = valor_total - desconto

# Resultados
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_a_pagar:.2f}")