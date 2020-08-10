"""
Similar to the code from the twitter_dag, but using a better DAG structure and 
airflow best practices 
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

import pull_data
import clean_data

############################################
# DEFINE AIRFLOW DAG (SETTINGS + SCHEDULE)
############################################

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    # 'email': [''],
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    # 'retries': 3,
    # 'retry_delay': timedelta(minutes=3),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2021, 1, 1),
}

dag = DAG( 
    dag_id="stock_dag", 
    default_args=default_args, 
    schedule_interval="@daily")  # <-- here we could also use a CRON expression - 0 0 * * *


##########################################
# DEFINE AIRFLOW OPERATORS
##########################################

pulling_data = PythonOperator(task_id="pulling_data", 
                                 python_callable=pull_data.main,
                                 dag=dag)


cleaning_data = PythonOperator(task_id="cleaning_data", 
                                   python_callable=clean_data.main,
                                   dag=dag) 


##########################################
# DEFINE TASKS HIERARCHY
##########################################

# define the dependencies for each task to make the directed graph 
pulling_data >> cleaning_data