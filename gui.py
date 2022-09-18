from tkinter import *
import pandas as pd

# GUI Constants
PADX = (25, 0)

# Strategy Constants
VERTICAL_SPREADS = [
    'Debit Call Spread',
    'Credit Call Spread',
    'Debit Put Spread',
    'Credit Put Spread'
]
STRATEGIES = [
    *VERTICAL_SPREADS,
]

calls_df = pd.read_csv('data/SPY_CALLS.csv')

def get_expiries():
    return calls_df['Expiry'].unique()

def get_strikes(expiry):
    return list(calls_df.loc[calls_df['Expiry'] == expiry, 'Strike'].unique())

def strategy_choice_callback(*_):
    def setup_vertical_spread():
        pass

    if strategy_var.get() in VERTICAL_SPREADS:
        pass

def setup_debit_call_spread(expiry):
    strikes = get_strikes(expiry_var.get())

    # Long Call (Lower Strike)
    long_call_lower_strike_label = Label(master, text='Long Call (Lower Strike)')
    long_call_lower_strike_label.pack(side=LEFT, anchor=NW, padx=PADX)

    long_call_lower_strike_var = IntVar(master)
    long_call_lower_strike_menu = OptionMenu(master, long_call_lower_strike_var, *strikes)
    long_call_lower_strike_menu.pack(side=LEFT, anchor=NW)

    # Short Call (Lower Strike)
    short_call_higher_strike_label = Label(master, text='Short Call (Higher Strike)')
    short_call_higher_strike_label.pack(side=LEFT, anchor=NW, padx=PADX)

    short_call_lower_strike_var = IntVar(master)
    short_call_lower_strike_menu = OptionMenu(master, short_call_lower_strike_var, *strikes)
    short_call_lower_strike_menu.pack(side=LEFT, anchor=NW)

def expiry_choice_callback(*_):
    if strategy_var.get() in VERTICAL_SPREADS:
        pass

    

    print(get_strikes(expiry_var.get()))
    setup_debit_call_spread(expiry_var.get())

def init():
    global master
    master = Tk()
    master.title("Equity Options Trading Toolkit")
    master.geometry('1280x720')

    global ticker_label
    ticker_label = Label(master, text='Underlying Ticker:')
    ticker_label.pack(side=LEFT, anchor=NW)

    ticker_var = StringVar(master)
    ticker_var.set('SPY')

    global ticker_menu
    ticker_menu = OptionMenu(master, ticker_var, *["SPY", "NVDA"])
    ticker_menu.pack(side=LEFT, anchor=NW)

    global strategy_var
    strategy_var = StringVar(master)
    strategy_var.set('Debit Call Spread')
    strategy_var.trace('w', strategy_choice_callback)

    strategy_label = Label(master, text='Strategy:')
    strategy_label.pack(side=LEFT, anchor=NW, padx=PADX)

    global strategy_menu
    strategy_menu = OptionMenu(master, strategy_var, *STRATEGIES)
    strategy_menu.pack(side=LEFT, anchor=NW)

    global expiry_label
    expiry_label = Label(master, text='Expiry:')
    expiry_label.pack(side=LEFT, anchor=NW, padx=PADX)

    global expiry_var
    expiry_var = StringVar(master)
    expiry_var.trace('w', expiry_choice_callback)

    global expiry_menu
    expiry_menu = OptionMenu(master, expiry_var, *get_expiries())
    expiry_menu.pack(side=LEFT, anchor=NW)

def main():
    init()
    master.mainloop()

if __name__ == "__main__":
    main()