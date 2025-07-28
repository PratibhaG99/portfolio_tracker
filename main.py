import yfinance as yahooFinance


def getStockValue(symbol, quantity):
    stock = yahooFinance.Ticker(symbol)
    current_price = stock.info.get('currenPrice', None)
    if current_price is None:
        current_price = stock.history(period="1d")['Close'][-1]
    return current_price * quantity


def getPortfolioValue(stocks):
    for stock in stocks:
        stock['quantity'] *= 2  
    total_value = sum(getStockValue(stock['symbol'], stock['quantity']) for stock in stocks)
    return total_value


stocks = [
    {"symbol": "AAPL", "quantity": 3},
    {"symbol": "GOOG", "quantity": 5},
    {"symbol": "TSLA", "quantity": 2},
]

portfolio_value = getPortfolioValue(stocks)

print("Portfolio Status:")
for stock in stocks:
    stock_value = getStockValue(stock['symbol'], stock['quantity'])
    print(
        f"Holding {stock['quantity'] // 2} shares of {stock['symbol']}, Total value: {stock_value}")

print(f"Total portfolio value: {portfolio_value}")
