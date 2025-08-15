<h1>Projeto: SQLite → Postgres (raw) → dbt (silver/gold) → Power BI usando Bonobo</h1>

<p>Este projeto implementa um pipeline <strong>ETL sem Docker</strong> para extração, carga, transformação e visualização de dados.</p>

<h2>🎯 Objetivo</h2>
<ul>
  <li><strong>Extrair</strong> dados de um banco <strong>SQLite</strong>.</li>
  <li><strong>Carregar</strong> os dados no <strong>Postgres</strong>, na camada <code>raw</code>.</li>
  <li><strong>Transformar</strong> os dados com <strong>dbt</strong> nas camadas <code>silver</code> e <code>gold</code>.</li>
  <li><strong>Consumir</strong> os dados no <strong>Power BI</strong>.</li>
</ul>

<h2>🚀 Fluxo Geral</h2>
<h3>Bonobo (Python)</h3>
<ul>
  <li>Conecta no SQLite.</li>
  <li>Lê todas as tabelas.</li>
  <li>Carrega no Postgres (schema <code>raw</code>).</li>
</ul>

<h3>dbt</h3>
<ul>
  <li>Usa os dados do schema <code>raw</code> como source.</li>
  <li>Cria tabelas limpas e tipadas na camada <code>silver</code>.</li>
  <li>Gera dimensões, fatos e métricas na camada <code>gold</code>.</li>
</ul>

<h3>Power BI</h3>
<ul>
  <li>Conecta na camada <code>gold</code> do Postgres.</li>
  <li>Monta dashboards e relatórios.</li>
</ul>

<h2>📂 Estrutura do Projeto</h2>
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

<h2>🛠 Tecnologias Utilizadas</h2>
<ul>
  <li>SQLite → Fonte de dados.</li>
  <li>Python + Bonobo → Orquestração e carga para Postgres.</li>
  <li>SQLAlchemy → Conexão com bancos.</li>
  <li>Pandas → Manipulação de dados durante o ETL.</li>
  <li>Postgres → Armazenamento nas camadas raw, silver, gold.</li>
  <li>dbt-core → Transformações de dados.</li>
  <li>Power BI → Visualização de dados.</li>
</ul>

<h2>⚙️ Configuração do Ambiente</h2>
<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3.8+</li>
  <li>Postgres instalado e rodando</li>
  <li>dbt-core e dbt-postgres instalados</li>
</ul>

<h3>Instalação dos pacotes</h3>
<pre>
pip install bonobo pandas sqlalchemy psycopg2-binary python-dotenv
pip install dbt-core dbt-postgres
</pre>

<h3>Configuração do .env</h3>
<pre>
SQLITE_PATH=./data/basketball.sqlite
PG_HOST=localhost
PG_PORT=5432
PG_DB=basketball
PG_USER=postgres
PG_PASSWORD=postgres
PG_SCHEMA_RAW=raw
</pre>

<h2>🔄 Execução do Pipeline</h2>
<ol>
  <li>Coloque o arquivo <code>basketball.sqlite</code> na pasta <code>data/</code>.</li>
  <li>Crie os schemas no Postgres:</li>
</ol>
<pre>
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;
</pre>
<ol start="3">
  <li>Execute o ETL:</li>
</ol>
<pre>
python run.py
</pre>
<ol start="4">
  <li>Rode as transformações no dbt:</li>
</ol>
<pre>
dbt run --profiles-dir profiles
</pre>

<h2>📊 Estrutura das Camadas</h2>
<ul>
  <li>raw → Dados brutos, extraídos diretamente do SQLite.</li>
  <li>silver → Dados limpos e tipados, prontos para análise.</li>
  <li>gold → Métricas e agregações otimizadas para BI.</li>
</ul>
