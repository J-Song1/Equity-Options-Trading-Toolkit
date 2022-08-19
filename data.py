import requests
import pandas as pd
from bs4 import BeautifulSoup

from constants import HEADERS

# TODO: Add Caching Functionality
def get_live_quote(
    type='all',
    strike: float=400.00,
    expiry_year: int=22,
    expiry_month: int=8,
    expiry_day: int=12,
    ):
    assert type in ['all', 'call', 'put']

    # Fetching Options Data from Yahoo Finance Webpage
    response = requests.get(
        'https://finance.yahoo.com/quote/SPY/options?date=1671148800',  #'https://finance.yahoo.com/quote/SPY/options', # TODO: Add Support for Static Dates
        headers=HEADERS,
        timeout=5 # TODO: Add Timeout Exception Handling
    )
    bsoup = BeautifulSoup(response.content, 'html.parser')
    tables = bsoup.find_all('table')

    # Options Data Cleaning
    dfs = pd.read_html(str(tables))
    for df in dfs:
        df.set_index('Strike', inplace=True)
        df['Volume'] = df['Volume'].replace('-', '0') .astype(int)
        df['Implied Volatility'] = df['Implied Volatility'].str.replace('%', '') .astype(float) / 100.0

        # TODO: Add Option Expiry for Later

    calls_df, puts_df = dfs

    return calls_df, puts_df