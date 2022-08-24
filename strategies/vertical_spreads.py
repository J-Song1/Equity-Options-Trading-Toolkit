# DO YOU NEED GUARDS FOR PYTHON???
from datetime import date, timedelta, datetime
import matplotlib.pyplot as plt
import numpy as np

from data import get_live_quote

def call_credit_spread(expiry: date, short_call_strike: int, long_call_strike: int):
    assert short_call_strike < long_call_strike

    calls_df, puts_df = get_live_quote()
    long_call = calls_df.loc[long_call_strike]
    short_call = calls_df.loc[short_call_strike]

    net_credit = short_call['Last Price'] - long_call['Last Price']
    max_gain = net_credit
    max_loss = short_call_strike - long_call_strike - net_credit
    print(net_credit, max_gain, max_loss)


# NOTE: May need to 'loosen' to 'float'?
def call_debit_spread(expiry: date, long_call_strike: float, short_call_strike: float):
    assert long_call_strike < short_call_strike
    strike_spread = short_call_strike - long_call_strike

    calls_df = get_live_quote(type='call')
    long_call = calls_df.loc[long_call_strike]
    short_call = calls_df.loc[short_call_strike]
    long_call_price = long_call['Last Price']
    short_call_price = short_call['Last Price']
    
    # Using 'Last Price' for Now - Need to Switch to Bid (Ask) for Short (Long)
    net_debit = long_call_price - short_call_price
    max_gain = strike_spread - net_debit
    max_loss = -net_debit

    # Long Call
    long_call_plot, = plt.plot([long_call_strike - 10, long_call_strike], [-long_call_price] * 2, 'g--', label=f'Long ${long_call_strike} Call')
    plt.plot([long_call_strike, short_call_strike + 10], [-long_call_price, -long_call_price + strike_spread + 10], 'g--')

    # Short Call
    short_call_plot, = plt.plot([long_call_strike - 10, short_call_strike], [short_call_price] * 2, 'r--', label=f'Short ${short_call_strike} Call')
    plt.plot([short_call_strike, short_call_strike + 10], [short_call_price, short_call_price - 10], 'r--')

    # Plotting "Call Debit Spread", "Long Call", "Short Call"
    call_spread_plot, = plt.plot([long_call_strike, short_call_strike], [max_loss, max_gain], 'b-', label='Call Debit Spread')
    plt.plot([long_call_strike - 10, long_call_strike], [max_loss] * 2, 'b-')
    plt.plot([short_call_strike, short_call_strike + 10], [max_gain] * 2, 'b-')

    plt.plot([long_call_strike - 10, short_call_strike + 10], [0] * 2, 'k-')

    plt.xlabel('$SPY at Expiry')
    plt.ylabel('Payoff')
    plt.legend(handles=[long_call_plot, short_call_plot, call_spread_plot])
    plt.show()

    expiry_datetime = calls_df.iloc[0].loc['Expiry'].to_pydatetime()

    time_to_expiry = expiry_datetime - datetime.today()
    print(type(time_to_expiry))
    print(net_debit, max_gain, max_loss)

def put_credit_spread(expiry: date, short_put_strike, long_put_strike):
    assert short_put_strike > long_put_strike

def put_debit_spread(expiry: date, long_put_strike: int, short_put_strike: int):
    assert long_put_strike > short_put_strike
