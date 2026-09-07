# Dados do aparelho
nome = input("Nome do aparelho: ")

# Entrada de dados do uso do aparelho
potência = float(input("Potência do aparelho (em Watts): "))
tempo_médio_uso = float(input("Tempo médio de uso diário (em horas): "))

# Consumo mensal
consumo_mensal = (potência * tempo_médio_uso * 30) / 1000

# Tarifa de energia elétrica
tarifa = 0.75

# Custo final
custo_estimado = consumo_mensal * tarifa

# Resultado
print(f"O consumo mensal do aparelho {nome} é de: {consumo_mensal:.2f} kWh.")
print(f"O custo estimado é de: R$ {custo_estimado:.2f}.")