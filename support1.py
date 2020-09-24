

def stock_history(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period = 'max')


def plot_history(ticker, start = None, end = None):
    if start and end:
        start_date, end_date = start, end
    else:
        start_date, end_date = ticker.index[0], ticker.index[-1]

    frame = ticker.loc[start_date:end_date]
    frame['Close'].plot(figsize = (15,5))
    plt.ylabel('Price')
    plt.show()

    start_price, end_price = frame.iloc[0]['Close'], frame.iloc[-1]['Close']
    print("Return: {:.2f}%".format((end_price - start_price)/start_price*100))



    asdfasdfasdfasdf
