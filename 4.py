# Valores de faturamento por estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o valor total de faturamento
faturamento_total = 0
for estado, valor in faturamento_por_estado.items():
    faturamento_total += valor

# Calcular e exibir o percentual de cada estado
print("Percentual de representação por estado:")
for estado, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
