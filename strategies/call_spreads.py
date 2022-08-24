
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