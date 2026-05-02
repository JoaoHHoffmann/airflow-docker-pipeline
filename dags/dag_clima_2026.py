from datetime import datetime
import pendulum
from airflow.models import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator

start_date=pendulum.datetime(2026, 1, 1, tz="UTC")

with DAG(
    dag_id="dag_clima_2026",
    start_date=start_date,
    schedule="@daily", 
) as dag:
    
    tarefa_1 = EmptyOperator(task_id="tarefa_1")
    tarefa_2 = EmptyOperator(task_id="tarefa_2")
    tarefa_3 = EmptyOperator(task_id="tarefa_3")
    tarefa_4 = BashOperator(
        task_id="cria_pasta",
        bash_command="mkdir -p /opt/airflow/data/raw/semana_{{ ds }}"
    )

    tarefa_1 >> [tarefa_2, tarefa_3]
    tarefa_3 >> tarefa_4


