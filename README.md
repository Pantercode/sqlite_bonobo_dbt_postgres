# sqlite_bonobo_dbt_postgres


# Projeto: SQLite → Postgres (raw) → dbt (silver/gold) → Power BI usando Bonobo

Este projeto implementa um pipeline **ETL sem Docker** para extração, carga, transformação e visualização de dados.  
O objetivo é:

1. **Extrair** dados de um banco **SQLite**.
2. **Carregar** os dados no **Postgres**, na camada **raw**.
3. **Transformar** os dados com **dbt** nas camadas **silver** (limpeza/tipagem) e **gold** (modelos prontos para BI).
4. **Consumir** os dados no **Power BI**.

---

## 🚀 Fluxo Geral

1. **Bonobo (Python)**  
   - Conecta no SQLite.
   - Lê todas as tabelas.
   - Carrega no Postgres (schema `raw`).
   
2. **dbt**  
   - Usa os dados do schema `raw` como **source**.
   - Cria tabelas limpas e tipadas na camada `silver`.
   - Gera dimensões, fatos e métricas na camada `gold`.

3. **Power BI**  
   - Conecta na camada `gold` do Postgres.
   - Monta dashboards e relatórios.

---

## 📂 Estrutura do Projeto

<pre>
sqlite-to-postgres-bonobo-dbt/
  data/
    basketball.sqlite        # Arquivo SQLite de origem
  etl/
    __init__.py              # Inicialização do módulo ETL
    config.py                # Configurações e variáveis de ambiente
    io_adapters.py           # Funções de conexão e leitura/escrita
    transforms.py            # Transformações de dados
    graph.py                 # Definição do grafo Bonobo (pipeline)
  .env                       # Configurações de ambiente
  run.py                     # Script principal do ETL
  README.md                  # Documentação do projeto
</pre>



---

## 🛠 Tecnologias Utilizadas

- **SQLite** → Fonte de dados.
- **Python + Bonobo** → Orquestração e carga para Postgres.
- **SQLAlchemy** → Conexão com bancos.
- **Pandas** → Manipulação de dados durante o ETL.
- **Postgres** → Armazenamento nas camadas `raw`, `silver`, `gold`.
- **dbt-core** → Transformações de dados.
- **Power BI** → Visualização de dados.

---

## ⚙️ Configuração do Ambiente

1. **Pré-requisitos**
   - Python 3.8+
   - Postgres instalado e rodando🔄 Execução do Pipeline

Coloque o arquivo basketball.sqlite na pasta data/.

Crie os schemas no Postgres:

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;


Execute o ETL com:

python run.py


Rode as transformações no dbt:

dbt run --profiles-dir profiles

📊 Estrutura das Camadas

raw → Dados brutos, extraídos diretamente do SQLite.

silver → Dados limpos e tipados, prontos para análise.

gold → Métricas e agregações otimizadas para BI.
   - dbt-core e dbt-postgres instalados

2. **Instalação dos pacotes**
   ```bash
   pip install bonobo pandas sqlalchemy psycopg2-binary python-dotenv
   pip install dbt-core dbt-postgres



   Configuração do .env

SQLITE_PATH=./data/basketball.sqlite
PG_HOST=localhost
PG_PORT=5432
PG_DB=basketball
PG_USER=postgres
PG_PASSWORD=postgres
PG_SCHEMA_RAW=raw

