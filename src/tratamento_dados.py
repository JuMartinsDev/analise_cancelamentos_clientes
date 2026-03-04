import pandas as pd

def carregar_dados(caminho):
    """
    Passo 1 e 2: Abrir a base de dados (importar) e visualizar
    - Entender as informações disponíveis
    - Remover informações que não ajudam (CustomerID)
    """
    df = pd.read_csv(caminho)
    
    # Removendo coluna irrelevante
    if "CustomerID" in df.columns:
        df = df.drop(columns="CustomerID")
    
    # Valores em formatos errados, informações vazias
    df = df.dropna()
    
    # Mostrar informações da base
    print(df.info())
    
    return df

def aplicar_filtros(df):
    """
    Passo 5: Filtrar a base de dados para análises detalhadas
    - duração do contrato diferente de 'Monthly'
    - ligações ao call center <= 4
    - dias de atraso <= 20
    """
    # todo mundo do contrato mensal cancelou o serviço, vamos dar desconto no plano anual e trimestral
    df = df[df["duracao_contrato"] != "Monthly"]

    # ligações_callcenter acima de 4 -> todo mundo cancelou, problema não resolvido
    # se algum cliente ligar 3x para o call center, alerta vermelho
    df = df[df["ligacoes_callcenter"] <= 4]

    # atraso no pagamento acima de 20 dias -> cliente cancela
    # se o cliente atrasar 15 dias no pagamento, alerta vermelho
    df = df[df["dias_atraso"] <= 20]
    
    return df