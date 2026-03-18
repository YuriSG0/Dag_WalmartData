from repositories.connecting_SQL import connecting_database
import pandas as pd
from dotenv import load_dotenv
import os
import numpy as np
from pathlib import Path

def save_dataframe():
    load_dotenv(Path(__file__).resolve().parent.parent / 'config' / '.env')
    engine = connecting_database()
    df_walmart = pd.read_sql_table(os.getenv('TABLE'),engine)
    return df_walmart

def add_column_profit_unit(df = pd.DataFrame):
    df['profit_unit'] = df['CPI'] - df['Fuel_Price']
    return df

def add_status_temperature(df = pd.DataFrame):
    df['Status_Temperature'] = np.select(
        [
             df['Temperature'] >= 50.0,
            (df['Temperature'] >= 20.0) & (df['Temperature'] < 50.0),
             df['Temperature'] < 20.0
        ],
        [ 
            'High',
            'Medium',
            'Bass',
        ],
        default = 'Unknown'
    )
    return df
