import pandas as pd

import pymysql
from sqlalchemy import create_engine
from investiny import historical_data, search_assets

nasdaq_top10 = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'TSLA']

for nas in nasdaq_top10:
    search_results = search_assets(query=nas, limit=1, type="Stock", exchange="NASDAQ")

    investing_id = int(search_results[0]["ticker"]) # Assuming the first entry is the desired one (top result in Investing.com)

    db_connection_str = 'mysql+pymysql://root:6569@localhost/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    data = historical_data(investing_id=investing_id,
                           from_date="01/01/2020",
                           to_date="10/16/2022")
    df=pd.DataFrame(data)
    df.date=pd.to_datetime(df.date,format='%m/%d/%Y')
    df.to_sql(name=f'us_{nas}', con=conn, if_exists='append',index=False)
