
from strategy import Strategy
from options import CallOption, PutOption

class LongStraddle(Strategy):
    def __init__(self, long_call: CallOption, long_put: PutOption):
        assert long_call.strike == long_put.strike, "Straddle"
        assert long_call.expiry == long_put.expiry, ""

        self.long_call = long_call
        self.long_put = long_put

class ShortStraddle(Strategy):
    def __init__(self, short_call: CallOption, short_put: PutOption):
        assert short_call.strike == short_put.strike, "Straddle"
        assert short_call.expiry == short_put.expiry, ""

        self.short_call = short_call
        self.short_put = short_put
    
