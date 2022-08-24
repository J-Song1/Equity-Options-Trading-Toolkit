from strategy import Strategy
from options import CallOption, PutOption

class NakedShortCall(Strategy):
    def __init__(self, short_call: CallOption):
        self.underlying = short_call.underlying
        self.short_call = short_call

        super().__init__(
            title=f'Naked Short \${self.underlying} Call: (\${short_call.strike}C)',
            net_premium=short_call.price
        )

    def show_plot(self, x_min=None, x_max=None):
        pass

class NakedShortPut(Strategy):
    def __init__(self, short_put: PutOption):
        self.underlying = short_put.underlying
        self.short_put = short_put

        super().__init__(
            title=f'Naked Short \${self.underlying} Put: (\${short_put.strike}P)',
            net_premium=short_put.price
        )

    def show_plot(self, x_min=None, x_max=None):
        pass