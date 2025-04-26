import sys

def ticker_symbols():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return

    ticker = sys.argv[1].upper()
    for company, symbol in COMPANIES.items():
        if symbol == ticker:
            print(f"{company} {STOCKS[symbol]}")
            return
    print("Unknown ticker")

if __name__ == '__main__':
    ticker_symbols()