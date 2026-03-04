def resumo_cancelamentos(df):
    """
    Passo 4: Análise inicial
    - Entender quantos clientes cancelaram
    - Mostrar porcentagem de cancelamentos

    Mostra análise detalhada do dataframe filtrado:
    - Quantidade e porcentagem de cancelamentos
    - Estatísticas de colunas numéricas
    - Distribuição de contratos, ligações e atrasos
    """
    print("\n===== QUANTIDADE DE CANCELAMENTOS =====")
    print(df["cancelou"].value_counts())

    print("\n===== PORCENTAGEM DE CANCELAMENTOS =====")
    print(df["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

    print("\n===== ESTATÍSTICAS GERAIS DAS COLUNAS NUMÉRICAS =====")
    print(df.describe())

    print("\n===== DISTRIBUIÇÃO DE CONTRATOS =====")
    if "duracao_contrato" in df.columns:
        print(df["duracao_contrato"].value_counts())
        print(df["duracao_contrato"].value_counts(normalize=True).map("{:.1%}".format))

    print("\n===== DISTRIBUIÇÃO DE LIGAÇÕES AO CALL CENTER =====")
    if "ligacoes_callcenter" in df.columns:
        print(df["ligacoes_callcenter"].value_counts())
    
    print("\n===== DISTRIBUIÇÃO DE DIAS DE ATRASO =====")
    if "dias_atraso" in df.columns:
        print(df["dias_atraso"].value_counts())