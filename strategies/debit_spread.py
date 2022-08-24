
# Public Libraries
import seaborn as sns
import matplotlib.pyplot as plt


from strategy import Strategy
from options import CallOption, PutOption

class CallDebitSpread(Strategy): # Bullish
    def __init__(self, long_call: CallOption, short_call: CallOption):
        assert long_call.underlying == short_call.underlying
        self.underlying = long_call.underlying
        
        assert long_call.strike < short_call.strike
        self.long_call = long_call
        self.short_call = short_call
        
        self.strike_spread = short_call.strike - long_call.strike

        super().__init__(
            title=f'\${self.underlying} Call Debit Spread: \${long_call.strike}C, (${short_call.strike}C)',
            net_premium=short_call.price - long_call.price
        )

    def plot_profit(self, s_min=None, s_max=None):
        if s_min is None: s_min = self.long_call.strike - 10
        if s_max is None: s_max = self.short_call.strike + 10
        assert s_min < self.long_call.strike
        assert s_max > self.short_call.strike

        super()._show_plot([
            (s_min, 0),
            (self.long_call.strike, 0),
            (self.short_call.strike, self.strike_spread),
            (s_max, self.strike_spread)
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

        """
        super()._show_plot([
            (s_min, ),
            ()
        ])
        """

def debug():
    """
    cds = CallDebitSpread(
        CallOption('SPY', 400, None, 100),
        CallOption('SPY', 450, None, 60)
    )
    cds.plot_profit()
    """

    cds = PutDebitSpread(
        PutOption('SPY', 450, None, 100),
        PutOption('SPY', 400, None, 60)
    )
    cds.show_plot()

if __name__ == '__main__':
    debug()