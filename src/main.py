from tratamento_dados import carregar_dados, aplicar_filtros
from analise_inicial import resumo_cancelamentos
from graficos import gerar_graficos

# Caminho da base
base = "./base/cancelamentos.csv"

# Passo 1, 2 e 3: Carregar e tratar dados
df = carregar_dados(base)

# Passo 5: Aplicar filtros detalhados
df = aplicar_filtros(df)

# Passo 4: Análise inicial
resumo_cancelamentos(df)

# Passo 5: Gerar gráficos detalhados (opcional)
gerar_graficos(df) 