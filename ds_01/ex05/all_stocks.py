import sys

def all_stocks():
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

    tickers = sys.argv[1].strip().split(',')
    if any(not tick.strip() for tick in tickers):
        return
    for tick in tickers:
        tick = tick.strip()
        tick_upper = tick.upper()
        if tick_upper in STOCKS:
            for company, symbol in COMPANIES.items():
                if symbol == tick_upper:
                    print(f"{symbol} is a ticker symbol for {company}")
                    break
        elif tick.capitalize() in COMPANIES:
            print(f"{tick.capitalize()} stock price is {STOCKS[COMPANIES[tick.capitalize()]]}")
        else:
            print(f"{tick} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()