# Análise de Cancelamentos de Clientes

## Objetivo

Este projeto tem como objetivo analisar os **cancelamentos de clientes**, identificar padrões e criar filtros que ajudam a entender o comportamento dos clientes que cancelam serviços.  
Ele aplica **regras de negócio**, realiza **estatísticas detalhadas** e apresenta gráficos para facilitar a visualização dos dados.

---

## Estrutura do Projeto

```

jornada_python/
│
├─ data/
│   └─ cancelamentos.csv         # Base de dados original
│
├─ src/
│   ├─ main.py                   # Script principal para rodar o projeto
│   ├─ tratamento_dados.py       # Funções de carregamento e tratamento de dados
│   ├─ analise_inicial.py        # Funções de análise e estatísticas
│   └─ graficos.py               # Funções para gerar gráficos
│
└─ requirements.txt              # Pacotes necessários

````

---

## Como Rodar

1. **Criar ambiente virtual (Windows PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate
````

2. **Instalar dependências:**

```powershell
pip install -r requirements.txt
```

3. **Rodar o projeto:**

```powershell
cd src
python main.py
```

---

## Resultados e Insights

Após o tratamento e filtragem dos dados, algumas observações foram identificadas:

* **Porcentagem de cancelamentos:** ~56% dos clientes cancelaram.
* **Duração do contrato:** Clientes com contrato mensal têm maior tendência a cancelar; descontos em planos trimestrais e anuais podem reduzir cancelamentos.
* **Ligação ao Call Center:** Clientes que ligaram mais de 4 vezes tendem a cancelar; se ligarem 3 vezes, é sinal de alerta.
* **Atraso no pagamento:** Atrasos acima de 20 dias aumentam a chance de cancelamento; atraso de 15 dias gera alerta.

**Estatísticas detalhadas das colunas numéricas:**

* Média, mínimo, máximo e desvio padrão de `dias_atraso`, `ligacoes_callcenter` e `total_gasto`.
* Distribuição de contratos, ligações e atrasos.

---

## Alguns gráficos

<img width="1158" height="502" alt="image" src="https://github.com/user-attachments/assets/f89daac5-c2f5-47d7-a15d-39b831184fbd" />
---
<img width="987" height="446" alt="image" src="https://github.com/user-attachments/assets/707f3297-5265-4718-94b6-68ccd82c41ab" />
---
<img width="1472" height="459" alt="image" src="https://github.com/user-attachments/assets/d941514b-9515-40ac-b3e4-3596e79e5f80" />
---
<img width="920" height="301" alt="image" src="https://github.com/user-attachments/assets/b4d91d8e-8690-4b10-b272-ed8738251229" />
---
<img width="988" height="333" alt="image" src="https://github.com/user-attachments/assets/ba28613a-508f-4c21-92db-075f61238ab2" />
---

## Conclusão

O projeto fornece uma **visão detalhada do perfil dos clientes que cancelam**, permitindo tomar decisões estratégicas, como:

* Ajustar planos para reduzir cancelamentos
* Monitorar clientes com múltiplas ligações ao call center
* Criar alertas para atrasos nos pagamentos

