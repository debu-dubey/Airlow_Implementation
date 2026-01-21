from airflow import DAG
from airflow.operators.python import PythonOperator
from datatime import datatime

dag = DAG(
    dag_id = 'my_first_dag',
    start_date = datetime(2026,1,18),
    schedule_interval = '@daily'
)


def print_hello():
    print('Hello from Airflow')

def email_boss():
    print("Email is sent to the client")


hello_Task = PythonOperator(task_id = 'first_task_in_the_dag', python_callable = print_hello)
email_task = PythonOperator(task_id = 'first email to the client', python_callable = email_boss)

#set the dependencies
hello_Task >> email_task