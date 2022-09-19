import os
import sys
sys.path.append('/Users/jsong/Documents/options-strats-market-making/')

from datetime import datetime, timedelta
from math import sqrt
from numpy import log, exp
from scipy.stats import norm

from utility.constants import CALENDAR_DAYS_IN_YEAR
from utility.risk_free_rates import get_risk_free_rate

import pandas as pd

class EquityOption:
    def __init__(self, 
        underlying: str, 
        strike: float, 
        expiry: datetime, 
        price: float, 
        volume: int=None, 
        open_interest: int=None
        ):

        self.underlying = underlying
        self.strike = strike
        self.expiry = expiry
        self.price = price
        self.volume = volume
        self.open_interest = open_interest
        self.implied_volatility = None

    def get_years_to_expiry(self, now: datetime) -> float:
        return (self.expiry - now) / timedelta(CALENDAR_DAYS_IN_YEAR) # TODO: Adjust for "Trading Days" Only

    def get_d1(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        numerator = log(spot / self.strike) + (risk_free_rate + pow(implied_volatility, 2) / 2) * years_to_expiry
        denominator = implied_volatility * sqrt(years_to_expiry)
        d1 = numerator / denominator
        return d1

    def get_d2(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)
        d2 = self.get_d1(spot, now, implied_volatility) - implied_volatility * sqrt(years_to_expiry)
        return d2

    def get_price(self):
        pass

    def get_delta(self, spot: float, now: datetime, implied_volatility: float):
        delta = norm.cdf(self.get_d1(spot, now, implied_volatility))
        return delta

    def get_gamma(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)

        numerator = norm.pdf(self.get_d1(spot, now, implied_volatility))
        denominator = spot * implied_volatility * sqrt(years_to_expiry)
        gamma = numerator / denominator
        return gamma

    def get_vega(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)

        vega = spot * norm.pdf(self.get_d1(spot, now, implied_volatility)) * sqrt(years_to_expiry) / 100.0
        return vega
    
    def get_theta(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        numerator = -spot * norm.pdf(self.get_d1(spot, now, implied_volatility)) * implied_volatility
        denominator = 2 * sqrt(years_to_expiry)
        term1 = numerator / denominator
        term2 = -risk_free_rate * self.strike * exp(-risk_free_rate * years_to_expiry) \
            * norm.cdf(self.get_d2(spot, now, implied_volatility))

        theta = (term1 + term2) / CALENDAR_DAYS_IN_YEAR
        return theta 

    def get_rho(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        rho = self.strike * years_to_expiry * exp(-risk_free_rate * years_to_expiry) \
            * norm.cdf(self.get_d2(spot, now, implied_volatility))
        return rho / 100.0

    # Numerical Method to Calcualte Implied Volatility, Given Price
    def fit_implied_volatility(self):
        if self.implied_volatility is not None: return

class CallOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float):
        super().__init__(underlying, strike, expiry, price)

class PutOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float):
        super().__init__(underlying, strike, expiry, price)

def series_to_option(series: pd.Series) -> EquityOption:
    print(series)
    underlying = 'SPY'
    strike = series['Strike']
    expiry = datetime.strptime(series['Expiry'], '%Y-%m-%d %H:%M:%S')
    price = series['Last Price']

    call = CallOption(underlying, strike, expiry, price)
    print('Delta', call.get_delta(385.56, datetime.now(), series['Implied Volatility']))
    print('Gamma', call.get_gamma(385.56, datetime.now(), series['Implied Volatility']))
    print('Theta', call.get_theta(385.56, datetime.now(), series['Implied Volatility']))
    print('Vega', call.get_vega(385.56, datetime.now(), series['Implied Volatility']))
    print('Rho', call.get_rho(385.56, datetime.now(), series['Implied Volatility']))

if __name__ == '__main__':
    df = pd.read_csv('resources/SPY_Calls.csv')
    option = df.loc[df['Contract Name'] == 'SPY221230C00400000'].iloc[0]

    #print(df.iloc[50], type(df.iloc[50]))
    print(series_to_option(option))

    