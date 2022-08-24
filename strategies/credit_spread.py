from strategy import Strategy
from options import CallOption, PutOption

class CallCreditSpread(Strategy): # Bearish
    def __init__(self, short_call: CallOption, long_call: CallOption):
        assert short_call.underlying == long_call.underlying
        self.underlying = short_call.underlying

        assert short_call.strike < long_call.strike
        self.short_call = short_call
        self.long_call = long_call

        self.strike_spread = short_call.strike - long_call.strike

        super().__init__(
            title=f'\${self.underlying} Call Credit Spread: (\${short_call.strike}C), \${long_call.strike}C',
            net_premium=self.short_call.price - self.long_call.price
        )

    def show_plot(self, s_min=None, s_max=None):
        if s_min is None: s_min = self.short_call.strike - 10
        if s_max is None: s_max = self.long_call.strike + 10
        assert s_min < self.short_call.strike
        assert s_max > self.long_call.strike

        super()._show_plot([
            (s_min, 0),
            (self.short_call.strike, 0),
            (self.long_call.strike, self.strike_spread),
            (s_max, self.strike_spread)
        ])

class PutCreditSpread(Strategy): # Bullish
    def __init__(self, short_put: PutOption, long_put: CallOption):
        assert short_put.underlying == long_put.underlying
        self.underlying = short_put.underlying

        assert short_put.strike > long_put.strike
        self.short_put = short_put
        self.long_put = long_put

        self.strike_spread = long_put.strike - short_put.strike

        super().__init__(
            title=f'\${self.underlying} Put Credit Spread: (\${self.short_put.strike}P), \${self.long_put.strike}P',
            net_premium=self.short_put.price - self.long_put.price
        )

    def show_plot(self, s_min=None, s_max=None):
        if s_min is None: s_min = self.long_put.strike - 10
        if s_max is None: s_max = self.short_put.strike + 10
        assert s_min < self.long_put.strike
        assert s_max > self.short_put.strike

        super()._show_plot([
            (s_min, self.strike_spread),
            (self.long_put.strike, self.strike_spread),
            (self.short_put.strike, 0),
            (s_max, 0)
        ])

def debug():
    """
    ccs = CallCreditSpread(
        CallOption('SPY', 400, None, 50),
        CallOption('SPY', 420, None, 35)   
    )
    ccs.show_plot()
    """

    pcs = PutCreditSpread(
        PutOption('SPY', 420, None, 50),
        PutOption('SPY', 400, None, 30)
    )
    pcs.show_plot()

if __name__ == '__main__':
    debug()