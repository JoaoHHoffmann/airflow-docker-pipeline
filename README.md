# airflow-docker-pipeline

Pipeline de dados orquestrado com Apache Airflow 3.2.1 rodando em Docker, usando CeleryExecutor com Redis e PostgreSQL.

## Estrutura

```
airflow-docker-pipeline/
├── dags/               
├── data/               
├── src/                
├── docker-compose.yaml 
└── requirements.txt    
```

## Como rodar

Antes de tudo, você vai precisar do Docker instalado com pelo menos 4GB de RAM disponíveis.

Clone o repositório e crie um arquivo `.env` na raiz com as seguintes variáveis:

```env
AIRFLOW_UID=50000
FERNET_KEY=sua_chave_aqui
```

Para gerar a Fernet Key, rode:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Depois, inicialize o ambiente e suba os serviços:

```bash
docker compose up airflow-init
docker compose up -d
```

A interface web estará disponível em `http://localhost:8080`. O usuário e senha padrão são `airflow`.

## Dependências

```
apache-airflow==3.2.1
pandas
requests
python-dotenv
```
