"""
File: greeks.py
Created: Aug 19, 2022
Modified: Aug 19, 2022
Description: "GREEKS"!!!
"""

# https://en.wikipedia.org/wiki/Black–Scholes_model
# Issue: Black-Scholes is for European Options - SPY Options are American-style

from datetime import datetime, timedelta
from math import sqrt
from numpy import log, exp
from scipy.stats import norm

from risk_free_rates import get_risk_free_rate
from constants import CALENDAR_DAYS_IN_YEAR

class Option:
    def __init__(self, expiry: datetime, strike: float):
        self.expiry = expiry
        self.strike = strike
        self.clear_cache()

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

        vega = spot * norm.pdf(self.get_d1(spot, now, implied_volatility)) * sqrt(years_to_expiry)
        return vega
    
    def get_theta(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        numerator = -spot * norm.pdf(self.get_d1(spot, now, implied_volatility)) * implied_volatility
        denominator = 2 * sqrt(years_to_expiry)
        term1 = numerator / denominator
        term2 = -risk_free_rate * self.strike * exp(-risk_free_rate * years_to_expiry) \
            * norm.cdf(self.get_d2(spot, now, implied_volatility))

        theta = term1 + term2
        return theta 

    def get_rho(self, spot: float, now: datetime, implied_volatility: float):
        years_to_expiry = self.get_years_to_expiry(now)
        risk_free_rate = get_risk_free_rate(years_to_expiry)

        rho = self.strike * years_to_expiry * exp(-risk_free_rate * years_to_expiry) \
            * norm.cdf(self.get_d2(spot, now, implied_volatility))
        return rho

    def get_implied_volatility(self) -> float:
        """
        Numeric Method to obtain Implied Volatility
        - Simple iterative method sufficies since 
          Black-Scholes Pricing Model/Function is 
          monotonically increasing with respect to IV.
        """

        pass

    def get_greeks(self, spot: float, now: datetime, implied_volatility: float):
        return {
            'delta': self.get_delta(),
            'gamma': self.get_gamma(),
            'vega': self.get_vega(),
            'theta': self.get_theta(),
            'rho': self.get_rho()
        }

        pass

    def get_years_to_expiry(self, now: datetime) -> float:
        return (self.expiry, now) / timedelta(CALENDAR_DAYS_IN_YEAR) # TODO: Adjust for "Trading Days" Only

    def clear_cache(self):
        self.delta = {}
        self.gamma = {}
        self.vega = {}
        self.theta = {}
        self.rho = {}

class CallOption(Option):
    def get_price(self):
        pass

    def get_theoretical_price(self):
        pass

class PutOption(Option):
    def get_price(self):
        pass

    def get_theoretical_price(self):
        pass

def debug():
    #x = get_d1(datetime.now(), datetime(2022, 12, 16, 16), 422.14, 425, 0.21144)
    #print(norm.cdf(x))

    x = get_d1(datetime.now(), datetime(2022, 12, 16, 16), 422.14, 460, 0.17153)
    print(norm.cdf(x))
    pass

if __name__ == '__main__':
    """
    Strike = 425
    Spot = 422.14
    expiry = December 16, 2022 4PM

    Implied Vol. = 0.21144    
    """
    debug()
