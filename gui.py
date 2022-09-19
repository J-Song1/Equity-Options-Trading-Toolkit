from tkinter import *
import pandas as pd
from strategies.call_spreads import CallDebitSpread
from PIL import ImageTk, Image  

from strategies.options import series_to_option

# GUI Constants
PADX = (25, 0)
FONT = ('Helvetica', 14, 'bold')
GREEN = '#008000'
RED = '#FF0000'


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

def calculate_setup_debit_call_spread(short_call_higher_strike_var, long_call_lower_strike_var, expiry_var):
    #print(short_call_higher_strike_var.get(), long_call_lower_strike_var.get())

    short_call_higher_strike = calls_df.loc[
        (calls_df['Expiry'] == expiry_var.get()) & (calls_df['Strike'] == short_call_higher_strike_var.get()),
    ].iloc[0]

    long_call_lower_strike = calls_df.loc[
        (calls_df['Expiry'] == expiry_var.get()) & (calls_df['Strike'] == long_call_lower_strike_var.get()),
    ].iloc[0]

    short_call = series_to_option(short_call_higher_strike)
    long_call = series_to_option(long_call_lower_strike)

    cds = CallDebitSpread(long_call, short_call)
    path = cds.plot_profit()
    image1 = Image.open(path)
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=25, y=200)

    # Do Greeks
    #greeks_frame = Frame(master)
    #greeks_frame.place(x=0, y=200)
    spot = 385

    delta_frame = Frame(master)
    delta_frame.place(x=30, y=50, anchor=N)
    Label(delta_frame, text='Delta', font=FONT).pack(side=TOP)
    Label(delta_frame, text=f'{short_call.get_delta():.4f}', font=FONT, fg=RED).pack(side=TOP)
    Label(delta_frame, text=f'{long_call.get_delta():.4f}', font=FONT, fg=GREEN).pack(side=TOP)
    Label(delta_frame, text=f'{cds.get_delta():.4f}', font=FONT).pack(side=TOP)

    gamma_frame = Frame(master)
    gamma_frame.place(x=95, y=50, anchor=N)
    Label(gamma_frame, text='Gamma', font=FONT).pack(side=TOP)
    Label(gamma_frame, text=f'{short_call.get_gamma():.4f}', font=FONT, fg=RED).pack(side=TOP)
    Label(gamma_frame, text=f'{long_call.get_gamma():.4f}', font=FONT, fg=GREEN).pack(side=TOP)
    Label(gamma_frame, text=f'{cds.get_gamma():.4f}', font=FONT).pack(side=TOP)

    theta_frame = Frame(master)
    theta_frame.place(x=160, y=50, anchor=N)
    Label(theta_frame, text='Theta', font=FONT).pack(side=TOP)
    Label(theta_frame, text=f'{short_call.get_theta():.4f}', font=FONT, fg=RED).pack(side=TOP)
    Label(theta_frame, text=f'{long_call.get_theta():.4f}', font=FONT, fg=GREEN).pack(side=TOP)
    Label(theta_frame, text=f'{cds.get_theta():.4f}', font=FONT).pack(side=TOP)

    vega_frame = Frame(master)
    vega_frame.place(x=225, y=50, anchor=N)
    Label(vega_frame, text='Vega', font=FONT).pack(side=TOP)
    Label(vega_frame, text=f'{short_call.get_vega():.4f}', font=FONT, fg=RED).pack(side=TOP)
    Label(vega_frame, text=f'{long_call.get_vega():.4f}', font=FONT, fg=GREEN).pack(side=TOP)
    Label(vega_frame, text=f'{cds.get_vega():.4f}', font=FONT).pack(side=TOP)

    rho_frame = Frame(master)
    rho_frame.place(x=290, y=50, anchor=N)
    Label(rho_frame, text='Rho', font=FONT).pack(side=TOP)
    Label(rho_frame, text=f'{short_call.get_rho():.4f}', font=FONT, fg=RED).pack(side=TOP)
    Label(rho_frame, text=f'{long_call.get_rho():.4f}', font=FONT, fg=GREEN).pack(side=TOP)
    Label(rho_frame, text=f'{cds.get_rho():.4f}', font=FONT).pack(side=TOP)

    price_frame = Frame(master)
    price_frame.place(x=355, y=50, anchor=N)
    Label(price_frame, text='Price', font=FONT).pack(side=TOP)
    Label(price_frame, text=f'{short_call.get_price():.4f}', font=FONT, fg=RED).pack(side=TOP)
    Label(price_frame, text=f'{long_call.get_price():.4f}', font=FONT, fg=GREEN).pack(side=TOP)
    Label(price_frame, text=f'{cds.get_price():.4f}', font=FONT).pack(side=TOP)

def setup_debit_call_spread(expiry):
    strikes = get_strikes(expiry_var.get())

    #strikes_frame = Frame(master)
    #strikes_frame.place(x=0, y=25)

    strike_labels_frame = Frame(master)
    strike_labels_frame.place(x=400, y=50)
    strike_menus_frame = Frame(master)
    strike_menus_frame.place(x=580, y=50)

    # Buffers
    Label(strike_labels_frame, text=' ', font=FONT).pack(side=TOP)
    Label(strike_menus_frame, text=' ', font=FONT).pack(side=TOP)

    # Short Call (Higher Strike)
    short_call_higher_strike_label = Label(strike_labels_frame, text='Short Call (Higher Strike)', font=FONT)
    short_call_higher_strike_label.pack(side=TOP, anchor=NW)

    short_call_higher_strike_var = IntVar(master, value=420)
    short_call_higher_strike_menu = OptionMenu(strike_menus_frame, short_call_higher_strike_var, *strikes)
    short_call_higher_strike_menu.pack(side=TOP, anchor=NE)

    # Long Call (Lower Strike)
    long_call_lower_strike_label = Label(strike_labels_frame, text='Long Call (Lower Strike)', font=FONT)
    long_call_lower_strike_label.pack(side=TOP, anchor=NW)

    long_call_lower_strike_var = IntVar(master, value=400)
    long_call_lower_strike_menu = OptionMenu(strike_menus_frame, long_call_lower_strike_var, *strikes)
    long_call_lower_strike_menu.pack(side=TOP, anchor=NE)

    Label(strike_labels_frame, text='Net Strategy', font=FONT).pack(side=TOP, anchor=NW)

    # Adding Button
    strategy_calculate = Button(
        strike_menus_frame, 
        text='Calculate', 
        command=lambda: calculate_setup_debit_call_spread(short_call_higher_strike_var, long_call_lower_strike_var, expiry_var)
    )
    strategy_calculate.pack(side=TOP, anchor=NE)

def expiry_choice_callback(*_):
    if strategy_var.get() == 'Debit Call Spread':
        setup_debit_call_spread(expiry_var.get())
    else:
        print('None')

def init():
    global master
    master = Tk()
    master.title("Equity Options Trading Toolkit")
    master.geometry('700x700')

    global ticker_label, ticker_menu
    ticker_label = Label(master, text='Underlying Ticker:', font=FONT)
    ticker_label.pack(side=LEFT, anchor=NW)

    ticker_var = StringVar(master, value='SPY')

    ticker_menu = OptionMenu(master, ticker_var, *["SPY", "NVDA"])
    ticker_menu.pack(side=LEFT, anchor=NW)

    global strategy_var
    strategy_var = StringVar(master, value=STRATEGIES[0])
    strategy_var.trace('w', strategy_choice_callback)

    strategy_label = Label(master, text='Strategy:', font=FONT)
    strategy_label.pack(side=LEFT, anchor=NW, padx=PADX)

    global strategy_menu
    strategy_menu = OptionMenu(master, strategy_var, *STRATEGIES)
    strategy_menu.pack(side=LEFT, anchor=NW)

    global expiry_label
    expiry_label = Label(master, text='Expiry:', font=FONT)
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