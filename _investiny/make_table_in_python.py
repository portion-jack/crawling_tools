import pymysql
import pandas as pd

from investiny import historical_data, search_assets
nasdaq_top10 = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'TSLA', 'BRK/A', 'BRK/B', 'UNH', 'JNJ']
kosdaq_top10 = ['Samsung Electronics Co Pref', 'Samsung Electronics Co', 'LG Energy Solution', 'SK Hynix Inc', 'LG Chem', 'Samsung Biologics', 'Hyundai Motor Co', 'Hyundai', 'Hyundai Motor Co Pref', 'LG Chemicals']
# space underbar replace
for i,kosdaq_top in enumerate(kosdaq_top10):
    kosdaq_top10[i] = kosdaq_top.replace(' ','_')

"""
search_results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ")
investing_id = int(search_results[0]["ticker"]) # Assuming the first entry is the desired one (top result in Investing.com)
data = historical_data(investing_id=investing_id,
                       from_date="10/10/2022",
                       to_date="10/16/2022")
df=pd.DataFrame(data)
"""

for exchange,nas_kos in zip(['us','kr'],[nasdaq_top10,kosdaq_top10]):
    for enterprice in nas_kos:
        try:
            conn = pymysql.connect(
                               user='root',
                               password='6569',
                               db='stock',
                               charset='utf8')

            sql = f"CREATE TABLE {exchange}_{enterprice}(" \
                  f"DATE    DATE    NOT NULL," \
                  f"OPEN    FLOAT   NOT NULL," \
                  f"HIGH    FLOAT   NOT NULL," \
                  f"LOW     FLOAT   NOT NULL," \
                  f"CLOSE   FLOAT   NOT NULL" \
                  f");"
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    conn.commit()
        except:
            pass
