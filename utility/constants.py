"""
File: constants.py
Author: Joon Song
Created: Aug 19, 2022
Modified: Aug 19, 2022
"""

from datetime import date, timedelta

# Yahoo Finance Website Constants
YFINANCE_URL = 'https://finance.yahoo.com'
YFINANCE_TIMEOUT = 5.0
DATE_QSTRING_REFERENCE = (
    date(2022, 8, 22),
    1661126400
)

# To "Emulate User Agent" - from Stackoverflow
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
TIMEOUT = 5.0

# CBOE Constants
CBOE_CLOSE = timedelta(hours=16) # 4:00 PM EST
CBOE_HOLIDAYS = [
    date(2022, 1, 17), # Martin Luther King, Jr. Day
    date(2022, 2, 21), # Presidents' Day
    date(2022, 4, 15), # Good Friday
    date(2022, 5, 30), # Memorial Day
    date(2022, 6, 20), # Juneteenth Holiday
    date(2022, 7, 4),  # Independence Day
    date(2022, 9, 5),  # Labor Day
    date(2022, 11, 24), # Thanksgiving Day
    date(2022, 11, 25), # Thanksgiving Early Close
    date(2022, 12, 26), # Christmas Day Observed
]

# Interest Rates
US_RATES_URL = 'http://www.worldgovernmentbonds.com/country/united-states/'
