from ast import Call
from strategies.options import PutOption
from strategy import Strategy
from options import CallOption, PutOption

class CallDebitSpread(Strategy): # Bullish
    def __init__(self, long_call: CallOption, short_call: CallOption):
        self.long_call = long_call
        self.short_call = short_call

class PutDebitSpread(Strategy): # Bearish
    def __init__(self, long_put: PutOption, short_put: PutOption):
        self.long_put = long_put
        self.short_put = short_put