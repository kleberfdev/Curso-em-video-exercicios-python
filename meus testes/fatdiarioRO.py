import json
import statistics

with open('C:/Users/ksfbi/Documentos/GitHub/Curso-em-video-exercicios-python/meus testes/faturamento_diario.json') as f:
    dados = json.load(f)
    faturamento_diario = dados['faturamento_diario']

# remover dias sem faturamento (valores iguais a 0)
faturamento_diario = [valor for valor in faturamento_diario.values() if valor > 0]

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = statistics.mean(faturamento_diario)
dias_acima_da_media = sum(valor > media_mensal for valor in faturamento_diario)

print(f"O menor valor de faturamento diário foi R${menor_valor:.2f}")
print(f"O maior valor de faturamento diário foi R${maior_valor:.2f}")
print(f"A média mensal de faturamento diário foi R${media_mensal:.2f}")
print(f"O número de dias com faturamento diário acima da média mensal foi {dias_acima_da_media}")
