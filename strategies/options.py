from datetime import datetime

class EquityOption:
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float, volume: int=None, open_interest: int=None):
        self.underlying = underlying
        self.strike = strike
        self.expiry = expiry
        self.price = price
        self.volume = volume
        self.open_interest = open_interest

class CallOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float):
        super().__init__(underlying, strike, expiry, price)

class PutOption(EquityOption):
    def __init__(self, underlying: str, strike: float, expiry: datetime, price: float):
        super().__init__(underlying, strike, expiry, price)