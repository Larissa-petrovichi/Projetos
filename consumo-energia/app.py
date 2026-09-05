nome = input("nome do aparelho: ")
potência = float(input("Potência do aparelho (em Watts): "))
tempo_médio_uso = float(input("Tempo médio de uso diário (em horas): "))
consumo_mensal = (potência * tempo_médio_uso * 30) / 1000
tarifa = 0.75
custo_estimado = consumo_mensal * tarifa
print(f"O consumo mensal do aparelho {nome} é de: {consumo_mensal:.2f} kWh.")
print(f"O custo estimado é de: R$ {custo_estimado:.2f}.")
