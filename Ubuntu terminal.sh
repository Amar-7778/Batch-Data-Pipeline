#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y
python3 -m venv ~/airflow_venv
source ~/airflow_venv/bin/activate
pip install apache-airflow pandas psycopg2-binary
airflow db init
airflow users create --username admin --firstname Amar --lastname User --role Admin --email admin@example.com
mkdir -p ~/airflow/dags/scripts
mkdir -p ~/airflow/data
cp /mnt/d/Projects/batch\ data\ pipeline/batch-etl-airflow/data/Customer_Transactions.csv ~/airflow/data/
nano ~/airflow/dags/sales_etl_dag.py
nano ~/airflow/dags/scripts/extract.py
nano ~/airflow/dags/scripts/transform.py
nano ~/airflow/dags/scripts/load.py
sudo service postgresql start
sudo -u postgres psql -c "\c customer_db" -c "GRANT ALL PRIVILEGES ON SCHEMA public TO postgres_user;" -c "GRANT CREATE ON SCHEMA public TO postgres_user;"
airflow scheduler
airflow webserver --port 8080
airflow dags list
deactivate