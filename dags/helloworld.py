from os import path
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def print_hello():
    return 'Hello world!'

default_args = {
    'owner': 'Oliver',
    'depends_on_past': False,
    'start_date': datetime(2019, 2, 1),
    'email': ['oliver@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('helloworld', description='hello world example', default_args=default_args, schedule_interval=timedelta(days=1), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

python_operator = PythonOperator(task_id='python_task', python_callable=print_hello, dag=dag)

bash_script = '/usr/local/airflow/scripts/hello_bash.sh'
if path.exists(bash_script):
    bash_operator = BashOperator(task_id='bash_task', bash_command=f"{bash_script} ", dag=dag)
    bash_operator.set_upstream(python_operator)

dummy_operator >> python_operator

