import os
from pathlib import Path
from sqlalchemy import text,create_engine
from dotenv import load_dotenv
import urllib


def connecting_database():
   try: 
        ##Loading variable ambient global 
        load_dotenv(Path(__file__).resolve().parent.parent / 'config' / '.env')

        conn = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={os.getenv('SERVER')};"
        f"DATABASE={os.getenv('DATABASE')};"
        "Trusted_Connection=yes;"
        ) 

        params = urllib.parse.quote_plus(conn)
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

        return engine

   except Exception as e:
       print('Conexão não Estabelecida !!')



