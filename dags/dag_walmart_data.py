from airflow import DAG,Dataset
from airflow.decorators import task
import pendulum
from datetime import timedelta
import pandas as pd
from repositories.load_data_transform import load_data_walmart
from src.process_transform_data import add_status_temperature,add_column_profit_unit,save_dataframe

default_arg = {
    "owner" : "airflow",
    "retries" :  3,
    "retry_delay" : timedelta(minutes = 2),
    "depends_on_past" : False
}

with DAG(
    dag_id = 'Walmart_ETL',
    description = ' Pepiline para a execucao de ETL dos dados do Walmart',
    schedule = None,
    default_args = default_arg,
    catchup = False,
    start_date = pendulum.datetime(2026,3,17,tz='America/Sao_Paulo')
) as dag : 
    
    @task
    def extraction_data_walmart(): 
        return save_dataframe()
    
    @task
    def transform_data_walmart(df = pd.DataFrame):
        df = add_column_profit_unit(df)
        df = add_status_temperature(df)
        return df
    
    @task
    def load_data_walmart_sales(df  = pd.DataFrame):
        load_data_walmart(df)

    extraction = extraction_data_walmart()
    transform = transform_data_walmart(extraction)
    load = load_data_walmart_sales(transform)

    extraction >> transform >> load

    
    

