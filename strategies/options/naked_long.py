# Add Imports
import matplotlib.pyplot as plt


class NakedLongCall:
    def __init__(self, ticker, expiry, strike, price=None):
        if price is None:
            pass

        self.ticker = ticker
        self.strike = strike
        self.expiry = expiry
        self.price = price
    
    def plot_payout(self, s_min=None, s_max=None, label=None):
        if s_min is None: s_min = self.strike - 10
        if s_max is None: s_max = self.strike + 20
        if label is None: label = f'Naked Long ${self.strike} {self.ticker} Call Payout'

        plt.plot([s_min, self.strike, s_max], [0, 0, s_max - self.strike], 'g--', label=label)
        #plt.show()

        """
        long_call_plot, = plt.plot([long_call_strike - 10, long_call_strike], [-long_call_price] * 2, 'g--', label=f'Long ${long_call_strike} Call')
        plt.plot([long_call_strike, short_call_strike + 10], [-long_call_price, -long_call_price + strike_spread + 10], 'g--')
        """

    def plot_profit(self, s_min=None, s_max=None, label=None):
        if s_min is None: s_min = self.strike - 10
        if s_max is None: s_max = self.strike + 20
        if label is None: label = f'Naked Long ${self.strike} {self.ticker} Call Profit'

        plt.plot([s_min, self.strike, s_max], [-self.price, -self.price, s_max - self.strike - self.price], 'g-', label=label)

class NakedLongPut:
    def __init__(self, expiry, strike, price=None):
        if price is None:
            pass

    def plot_payout(self):
        pass

    def plot_profit(self):
        pass


def debug():
    x = NakedLongCall('SPY', None, 400, 20)
    x.plot_payout()
    x.plot_profit()
    plt.show()
    pass

if __name__ == '__main__':
    debug()