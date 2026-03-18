from connecting_SQL import connecting_database
import pandas as pd

def load_data_walmart(df = pd.Dataframe):
    engine = connecting_database()
    df.to_sql(
        'Walmart_Gold',
         conn = engine,
         if_exists = 'append',
         index = False
    )