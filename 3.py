import json

with open('faturamento.json', 'r') as file:
    json_data = json.load(file)

def calcular_faturamento(json_data):
    faturamento_diario = json_data['faturamento_diario']
    
    menor_faturamento = None
    maior_faturamento = None
    soma_faturamento = 0
    dias_com_faturamento = 0

    # Iterar sobre cada dia para calcular o menor, maior e somar o faturamento
    for registro in faturamento_diario:
        valor = registro['valor']

        if valor > 0:
            if menor_faturamento is None or valor < menor_faturamento:
                menor_faturamento = valor
            if maior_faturamento is None or valor > maior_faturamento:
                maior_faturamento = valor
            soma_faturamento += valor
            dias_com_faturamento += 1

    # Calcular a média mensal de faturamento
    if dias_com_faturamento > 0:
        media_mensal = soma_faturamento / dias_com_faturamento
    else:
        media_mensal = 0

    # Contar os dias em que o faturamento foi superior à média
    dias_acima_da_media = 0
    for registro in faturamento_diario:
        valor = registro['valor']
        if valor > 0 and valor > media_mensal:
            dias_acima_da_media += 1

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima_media = calcular_faturamento(json_data)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
