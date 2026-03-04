# Passo a passo do projeto
# Passo 1: Abrir a base de dados (importar) - pip install pandas openpyxl nbformat ipykernel plotly
import pandas as pd
import plotly.express as px #gráficos

tabela = "./base/cancelamentos.csv"
df = pd.read_csv(tabela)

# Passo 2: Visualizar a base de dados
    # entender as informações disponíveis - informações que não te ajudam, te atrapalham - possíveis problemas/erros na base de dados
df = df.drop(columns="CustomerID")

# Passo 3: Corrigir os problemas da base de dados (tratamento de dados)
    # Valores em formatos errados, informações vazias
df = df.dropna()
print(df.info())

# Passo 4: Análise inicial (entender quantos clientes cancelaram)
print("\n")
print("Quantidade de cancelamentos")
print(df["cancelou"].value_counts())

print("\n")
print("Porcentagem de cancelamentos")
print(df["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise detalhada (causa do cancelamento dos clientes, como cada coluna impacta no cancelamento)
#cricação e exibição dos gráficos
# for coluna in df.columns:
#     graficoCancelamento = px.histogram(df, x=coluna, color="cancelou", text_auto=True)
#     graficoCancelamento.show()

    # todo mundo do contrato mensal caneclu o serviço, vamos dae desconto no plano anual e trimestrak
    # ligacoes_callcenter acima de 4, todo mundo cancelou, se aluem probelma que nn estamos conseguindo resolver
    #se algum cliente ligar 3x pro call centr, alerta vermlho

    #atraso no pagamento acima de 20 da cliente cancela, o cluente cancela,
    #se o cliente atrasar 15 dias no apagemn, alerta vermelh

#cancelamento = 56%
#filtrar base de dados
#duração_callcenter - > diferente de monthly
condicao = df["duracao_contrato"] != "Monthly"
df = df[condicao]
print(df)

#ligacoes_callcenter -> menores ou igual a 4
condicao = df["ligacoes_callcenter"] <=4
df = df[condicao]
print(df)

#dias_atraso -> menoresou igual a 20
condicao = df["dias_atraso"] <= 20
df = df[condicao]
print(df)

print(df["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
