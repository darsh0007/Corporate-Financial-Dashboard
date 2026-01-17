import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# Declaring server and DB names
SERVER = 'DARSHAN' 
DATABASE = 'CorporateFinanceDB'
DRIVER = 'ODBC Driver 17 for SQL Server'

# Connection String
conn_str = f'mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes'
engine = create_engine(conn_str)

def clean_currency(x):

    if isinstance(x, str):
        x = x.replace('$', '').replace(',', '').replace(' ', '') #'$ 1,200.50' -> 1200.50
        if x == '-':       #'$-' -> 0.0
            return 0.0
        try:
            return float(x)
        except:
            return 0.0
    return x

def run_etl():
    print("Starting ETL Process...")
    
    # Reading the raw messy CSV as STRING first to handle the '$' symbol
    df = pd.read_csv('Financial_Sample.csv', dtype=str)
    print(f"   -> Extracted {len(df)} rows from CSV.")

 # Adding _ if there are spaces between words
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    
    # List of numeric columns
    money_cols = ['manufacturing_price', 'sale_price', 'gross_sales', 
                  'discounts', 'sales', 'cogs', 'profit']
    
    for col in money_cols:
        df[col] = df[col].apply(clean_currency)

    # Fixing Date Column (SQL needs YYYY-MM-DD)
    df['date'] = pd.to_datetime(df['date'])

    print("   -> Data cleaning complete.")

    # LOAD will Push to SQL Server
    # 'replace' will drop the table if it exists and create a new one automatically
    table_name = 'Raw_Sales_Data'
    df.to_sql(table_name, engine, if_exists='replace', index=False)  #drop the existing one and create a new one
    
    print(f"Success! Data loaded into SQL table: {table_name}")

if __name__ == "__main__":
    run_etl()