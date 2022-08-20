from re import L
import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup

from constants import HEADERS, DATE_QSTRING_REFERENCE, YFINANCE_TIMEOUT, YFINANCE_URL

# For Yahoo Finance
def format_expiry_qstring(expiry: date) -> int:
    ref_date, ref_qstring = DATE_QSTRING_REFERENCE
    date_delta = expiry - ref_date

    expiry_qstring = ref_qstring + date_delta.days * 24 * 60 * 60 # Delta in Seconds
    return expiry_qstring

def get_options_chain_data(expiry: date, ticker: str='SPY') -> tuple[pd.DataFrame, pd.DataFrame]:
    assert ticker in ['SPY'] # Valid Ticker Assertion

    try:
        response = requests.get(
            f'{YFINANCE_URL}/quote/SPY/options?date={format_expiry_qstring(expiry)}',
            headers=HEADERS,
            timeout=YFINANCE_TIMEOUT,
        )
        bsoup = BeautifulSoup(response.content, 'html.parser')
        tables = bsoup.find_all('table')

        # Options Data Cleaning
        dfs = pd.read_html(str(tables))
        for df in dfs:
            df['Bid'] = df['Bid'].replace('-', '0').astype(float)
            df['Ask'] = df['Ask'].replace('-', '0').astype(float)
            df['Volume'] = df['Volume'].replace('-', '0') .astype(int)
            df['Expiry'] = datetime(expiry.year, expiry.month, expiry.day, 16)
            df['Open Interest'] = df['Open Interest'].replace('-', '0').astype(int)
            df['Implied Volatility'] = df['Implied Volatility'].str.replace('%', '') .astype(float) / 100.0

            df['Quote'] = datetime.now()
            df.set_index(['Strike', 'Expiry'], inplace=True)

        calls_df, puts_df = dfs
        return calls_df, puts_df

    except requests.exceptions.ReadTimeout:
        return None

def get_options_chain_data_batch(expiries: list[date], ticker: str='SPY') -> tuple[pd.DataFrame, pd.DataFrame]:
    assert ticker in ['SPY'] # Valid Ticker Assertion

    all_calls_df, all_puts_df = None, None
    for expiry in expiries:
        calls_df, puts_df = get_options_chain_data(expiry, ticker)
        all_calls_df = pd.concat([all_calls_df, calls_df])
        all_puts_df = pd.concat([all_puts_df, puts_df])
        print(len(all_calls_df), len(all_puts_df))
    
    return all_calls_df, all_puts_df

def get_options_chain_expiries(ticker: str='SPY') -> list[datetime]:
    assert ticker in ['SPY'] # Valid Ticker Assertion

    try:
        response = requests.get(
            f'{YFINANCE_URL}/quote/{ticker}/options',
            headers=HEADERS,
            timeout=YFINANCE_TIMEOUT,
        )
        bsoup = BeautifulSoup(response.content, 'html.parser')
        return [
            datetime.strptime(date_str.text, '%B %d, %Y').date() 
            for date_str in bsoup.find_all('select')[0]
        ]

    except requests.exceptions.ReadTimeout:
        return None

if __name__ == '__main__':
    expiries = get_options_chain_expiries()
    #print(expiries[0])
    print(get_options_chain_data(expiries[0])[0]['Quote'])
    #print(get_options_chain_data_batch(expiries))
