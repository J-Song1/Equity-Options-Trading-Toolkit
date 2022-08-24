from strategy import Strategy
from options import CallOption, PutOption

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


class PutDebitSpread(Strategy): # Bearish
    def __init__(self, long_put: PutOption, short_put: PutOption):
        assert long_put.underlying == short_put.underlying
        self.underlying = long_put.underlying

        assert long_put.strike > short_put.strike
        self.long_put = long_put
        self.short_put = short_put

        self.strike_spread = long_put.strike - short_put.strike

        super().__init__(
            title=f'\${self.underlying} Put Debit Spread: \${long_put.strike}P, (${short_put.strike}P)',
            net_premium=short_put.price - long_put.price
        )

    def show_plot(self, x_min=None, x_max=None):
        if x_min is None: x_min = self.short_put.strike - 10
        if x_max is None: x_max = self.long_put.strike + 10
        assert x_min < self.short_put.strike and x_max > self.long_put.strike

        super()._show_plot([
            (x_min, self.strike_spread),
            (self.short_put.strike, self.strike_spread),
            (self.long_put.strike, 0),
            (x_max, 0),
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