# inverstiny baseline
"""
from investiny import historical_data, search_assets

search_results = search_assets(query="AAPL", limit=1, type="Stock", exchange="NASDAQ")
investing_id = int(search_results[0]["ticker"]) # Assuming the first entry is the desired one (top result in Investing.com)

data = historical_data(investing_id=investing_id,
                       from_date="10/10/2022",
                       to_date="10/16/2022")

import pandas as pd


print("--NASDAQ : AAPL --")
print(pd.DataFrame(data).iloc[::-1])
"""
