import plotly.express as px

def gerar_graficos(df):
    """
    Passo 5: Análise detalhada (causa do cancelamento dos clientes)
    - Como cada coluna impacta no cancelamento
    - Exibe um gráfico de cada vez
    """
    # Lista de colunas que você quer analisar
    colunas = ["assinatura", "duracao_contrato", "total_gasto", "meses_ultima_interacao"]

    for coluna in colunas:
        # Detecta se a coluna é numérica ou categórica
        if df[coluna].dtype == "object":
            # Categórica
            grafico = px.histogram(
                df, 
                x=coluna, 
                color="cancelou", 
                text_auto=True,
                title=f"Análise de {coluna} (categórica)"
            )
        else:
            # Numérica: usa bins para não sobrecarregar
            grafico = px.histogram(
                df, 
                x=coluna, 
                color="cancelou", 
                nbins=20,   # 20 intervalos
                text_auto=True,
                title=f"Análise de {coluna} (numérica)"
            )

        # Exibe gráfico
        grafico.show()

        # Pausa até usuário apertar Enter
        input(f"Gráfico de {coluna} exibido. Pressione Enter para ver o próximo gráfico...")