import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(__file__))

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

FILE_PATH = r"D:\Projects\batch data pipeline\batch-etl-airflow\data\customer_transactions.csv"

def run_etl():
    print("🚀 ETL Job Started")

    df = extract_data(FILE_PATH)
    df_transformed = transform_data(df)
    load_data(df_transformed)

    print("✅ ETL Job Finished Successfully")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="customer_batch_etl",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["batch", "etl", "customer"]
) as dag:

    run_customer_etl = PythonOperator(
        task_id="run_customer_etl",
        python_callable=run_etl
    )
