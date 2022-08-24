# Add Imports
import matplotlib.pyplot as plt
from strategy import Strategy
from options import CallOption, PutOption

class NakedLongCall(Strategy):
    def __init__(self, long_call: CallOption):
        self.long_call = long_call
    
    def plot_payout(self, s_min=None, s_max=None, label=None, fmt='g--'):
        # Default Values
        if s_min is None: s_min = self.long_call.strike - 10
        if s_max is None: s_max = self.long_call.strike + 20
        if label is None: label = f'Naked Long {self.long_call.underlying} ${self.long_call.strike} Call Payout'

        plt.plot(
            [s_min, self.long_call.strike, s_max], 
            [0, 0, s_max - self.long_call.strike], 
            fmt, 
            label=label
        )

    def plot_profit(self, s_min=None, s_max=None, label=None, fmt='g-'):
        # Default Values
        if s_min is None: s_min = self.long_call.strike - 10
        if s_max is None: s_max = self.long_call.strike + 20
        if label is None: label = f'Naked Long {self.long_call.underlying} ${self.long_call.strike} Call Profit'

        plt.plot(
            [s_min, self.long_call.strike, s_max], 
            [-self.long_call.price, -self.long_call.price, s_max - self.long_call.strike - self.long_call.price], 
            fmt,
            label=label
        )

class NakedLongPut(Strategy):
    def __init__(self, long_put: PutOption):
        self.long_put = long_put

    def plot_payout(self, s_min=None, s_max=None, label=None, fmt='g--'):
        # Default Values
        if s_min is None: s_min = self.long_put.strike - 20
        if s_max is None: s_max = self.long_put.strike + 10
        if label is None: label = f'Naked Long {self.long_put.underlying} ${self.long_put.strike} Put Payout'

        plt.plot(
            [s_min, self.long_put.strike, s_max], 
            [self.long_put.strike - s_min, 0, 0], 
            fmt, 
            label=label
        )

    def plot_profit(self, s_min=None, s_max=None, label=None, fmt='g-'):
        # Default Values
        if s_min is None: s_min = self.long_put.strike - 20
        if s_max is None: s_max = self.long_put.strike + 10
        if label is None: label = f'Naked Long {self.long_put.underlying} ${self.long_put.strike} Put Profit'

        plt.plot(
            [s_min, self.long_put.strike, s_max], 
            [self.long_put.strike - s_min - self.long_put.price, -self.long_put.price, -self.long_put.price], 
            fmt, 
            label=label
        )

def debug():
    #x = NakedLongCall(CallOption('SPY', 400, None, 10))
    #x.plot_payout()
    #x.plot_profit()
    y = NakedLongPut(PutOption('SPY', 400, None, 10))
    y.plot_payout()
    y.plot_profit()
    plt.show()

if __name__ == '__main__':
    debug()