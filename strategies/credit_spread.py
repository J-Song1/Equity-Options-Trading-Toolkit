from strategy import Strategy
from options import CallOption, PutOption

class CallCreditSpread(Strategy): # Bearish
    def __init__(self, short_call: CallOption, long_call: CallOption):
        self.short_call = short_call
        self.long_call = long_call

class PutCreditSpread(Strategy): # Bullish
    def __init__(self, short_put: PutOption, long_put: CallOption):
        self.short_put = short_put
        self.long_put = long_put
