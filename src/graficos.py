import plotly.express as px

def gerar_graficos(df):
    """
    Passo 5: Análise detalhada (causa do cancelamento dos clientes)
    - Como cada coluna impacta no cancelamento
    """
    for coluna in df.columns:
        if coluna != "cancelou":
            grafico = px.histogram(df, x=coluna, color="cancelou", text_auto=True)
            grafico.show()