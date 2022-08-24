from datetime import datetime

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

    # Numerical Method to Calcualte Implied Volatility, Given Price
    def fit_implied_volatility(self):
        if self.implied_volatility is not None: return


class CallOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float):
        super().__init__(underlying, strike, expiry, price)

class PutOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float):
        super().__init__(underlying, strike, expiry, price)