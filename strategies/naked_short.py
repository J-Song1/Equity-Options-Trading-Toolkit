from strategy import Strategy
from options import CallOption, PutOption

class NakedShortCall(Strategy):
    def __init__(self, short_call: CallOption):
        self.short_call = short_call

class NakedShortPut(Strategy):
    def __init__(self, short_put: PutOption):
        self.short_put = short_put
