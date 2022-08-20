"""
File: risk_free_rates.py
Created: Aug 19, 2022
Modified: Aug 20, 2022
Description: Internal API for risk-free rates (US Treasuries)
"""
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from scipy.interpolate import CubicSpline # TODO: Look into actual yield-curve interpolation methods

from bs4 import BeautifulSoup
from constants import US_RATES_URL, HEADERS, TIMEOUT

# TODO: Add Caching
def get_us_treasury_rates(verbose=False):
    response = requests.get(
        url=US_RATES_URL,
        headers=HEADERS,
        timeout=TIMEOUT
    )
    bsoup = BeautifulSoup(response.content, 'html.parser')
    tables = bsoup.find_all('table')

    us_rates_df = pd.read_html(str(tables))[0]
    us_rates_df.columns = us_rates_df.columns.droplevel()
    us_rates_df = us_rates_df.loc[:, ['ResidualMaturity', 'Last']]
    us_rates_df.columns = ['Maturity', 'Yield', 'Price']
    us_rates_df['Yield'] = us_rates_df['Yield'].str.replace('%', '').astype(float) / 100.0
    us_rates_df['Years'] = pd.Series([1/12, 2/12, 3/12, 6/12, 1, 2, 3, 5, 7, 10, 20, 30])
    #us_rates_df.set_index('Maturity', inplace=True)

    if verbose:
        plt.plot(us_rates_df['Years'][:-2], us_rates_df['Yield'][:-2], marker='.')
        plt.xlabel('Time to Maturity (in Years)')

        plt.show()

    return us_rates_df

def get_risk_free_rate(maturity, region='us'):
    """
    Uses Cubic-Spline Interpolation
    """
    assert region in ['us'] and 0 <= maturity

    maturities, rates = zip(*US_RATES)
    # maturity_range = np.linspace(0, 30, 360)

    yield_curve_cs = CubicSpline(maturities, rates)

    return yield_curve_cs(maturity)


def debug():
    get_us_treasury_rates(True)

if __name__ == '__main__':
    debug()