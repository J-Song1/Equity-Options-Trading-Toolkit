# Add Imports
from pickletools import long1
import matplotlib.pyplot as plt
from strategy import Strategy
from options import CallOption, PutOption

class NakedLongCall(Strategy): # Bullish
    def __init__(self, long_call: CallOption):
        self.underlying = long_call.underlying
        self.long_call = long_call

        super().__init__(
            title=f'Naked Long \${self.underlying} Call: \${long_call.strike}C',
            net_premium=-long_call.price
        )
    
    def show_plot(self, x_min=None, x_max=None):
        if x_min is None: x_min = self.long_call.strike - 10
        if x_max is None: x_max = self.long_call.strike + 20
        assert x_min < self.long_call.strike and x_max > self.long_call.strike

class NakedLongPut(Strategy): # Bearish
    def __init__(self, long_put: PutOption):
        self.underlying = long_put.underlying
        self.long_put = long_put

        super().__init__(
            title=f'Naked Long \${self.underlying} Put: \${long_put.strike}P',
            net_premium=-long_put.price
        )

    def show_plot(self, x_min=None, x_max=None):
        if x_min is None: x_min = self.long_put.strike - 20
        if x_max is None: x_max = self.long_put.strike + 10
        assert x_min < self.long_put.strike and x_max > self.long_put.strike

def debug():
    """
    #x = NakedLongCall(CallOption('SPY', 400, None, 10))
    #x.plot_payout()
    #x.plot_profit()
    y = NakedLongPut(PutOption('SPY', 400, None, 10))
    y.plot_payout()
    y.plot_profit()
    plt.show()
    """

if __name__ == '__main__':
    debug()