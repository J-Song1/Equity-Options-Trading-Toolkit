"""
List of Dependencies (for Docker later):
- requests
- pandas
- bs4
"""

from datetime import date
from spreads.vertical_spreads import call_debit_spread, call_credit_spread

def main():
    #call_credit_spread(date.today(), 420, 450)
    call_debit_spread(date.today(), 420, 450)

if __name__ == '__main__':
    main()