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
        implied_vol: float,
        volume: int=None, 
        open_interest: int=None
        ):

        self.underlying = underlying
        self.strike = strike
        self.expiry = expiry
        self.price = price
        self.volume = volume
        self.open_interest = open_interest
        self.implied_vol = implied_vol

    def get_years_to_expiry(self) -> float:
        return (self.expiry - datetime.now()) / timedelta(CALENDAR_DAYS_IN_YEAR) # TODO: Adjust for "Trading Days" Only

    def get_spot(self):
        return 385.29

    def get_d1(self):
        years_to_expiry = self.get_years_to_expiry()
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        numerator = log(self.get_spot() / self.strike) + (risk_free_rate + pow(self.implied_vol, 2) / 2) * years_to_expiry
        denominator = self.implied_vol * sqrt(years_to_expiry)
        d1 = numerator / denominator
        return d1

    def get_d2(self):
        years_to_expiry = self.get_years_to_expiry()
        d2 = self.get_d1() - self.implied_vol * sqrt(years_to_expiry)
        return d2

    def get_price(self):
        return self.price

    def get_delta(self):
        delta = norm.cdf(self.get_d1())
        return delta

    def get_gamma(self):
        years_to_expiry = self.get_years_to_expiry()

        numerator = norm.pdf(self.get_d1())
        denominator = self.get_spot() * self.implied_vol * sqrt(years_to_expiry)
        gamma = numerator / denominator
        return gamma

    def get_vega(self):
        years_to_expiry = self.get_years_to_expiry()

        vega = self.get_spot() * norm.pdf(self.get_d1()) * sqrt(years_to_expiry) / 100.0
        return vega
    
    def get_theta(self):
        years_to_expiry = self.get_years_to_expiry()
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        numerator = -self.get_spot() * norm.pdf(self.get_d1()) * self.implied_vol
        denominator = 2 * sqrt(years_to_expiry)
        term1 = numerator / denominator
        term2 = -risk_free_rate * self.strike * exp(-risk_free_rate * years_to_expiry) \
            * norm.cdf(self.get_d2())

        theta = (term1 + term2) / CALENDAR_DAYS_IN_YEAR
        return theta 

    def get_rho(self):
        years_to_expiry = self.get_years_to_expiry()
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        rho = self.strike * years_to_expiry * exp(-risk_free_rate * years_to_expiry) \
            * norm.cdf(self.get_d2())
        return rho / 100.0

    # Numerical Method to Calcualte Implied Volatility, Given Price
    def fit_implied_volatility(self):
        if self.implied_volatility is not None: return

class CallOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float, implied_vol: float):
        super().__init__(underlying, strike, expiry, price, implied_vol)

class PutOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float, implied_vol: float):
        super().__init__(underlying, strike, expiry, price, implied_vol)

def series_to_option(series: pd.Series) -> EquityOption:
    print(series)
    underlying = 'SPY'
    strike = series['Strike']
    expiry = datetime.strptime(series['Expiry'], '%Y-%m-%d')
    price = series['Last Price']
    implied_vol = series['Implied Volatility']

    spot = 385.56

    call = CallOption(underlying, strike, expiry, price, implied_vol)
    return call

if __name__ == '__main__':
    df = pd.read_csv('resources/SPY_Calls.csv')
    option = df.loc[df['Contract Name'] == 'SPY221230C00400000'].iloc[0]

    #print(df.iloc[50], type(df.iloc[50]))
    print(series_to_option(option))

    