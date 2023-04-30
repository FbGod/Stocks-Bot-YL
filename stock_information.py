import io
from datetime import date, timedelta

import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from PIL import Image

sns.set()


# Информация + график котировок
def get_stock(ticker):
    end_date = date.today()
    start_date = end_date - timedelta(days=365)
    e = end_date.strftime("%Y-%#m-%#d")
    s = start_date.strftime("%Y-%#m-%#d")
    data = yf.download(tickers=ticker,
                       start=s, end=e, auto_adjust=True)
    plt.figure(figsize=(14, 10))
    sns.set_style("ticks")
    sns.lineplot(data=data, x="Date", y='Close', color='firebrick')
    sns.despine()
    plt.title(ticker, size='x-large', color='blue')
    info = yf.Ticker(ticker).info
    currency = info['currency']
    try:
        market_price = info['currentPrice']
    except KeyError:
        market_price = info['previousClose']
    name = info['shortName']
    try:
        comp = info['industry']
    except KeyError:
        comp = 'No type'
    try:
        recs = '\n' + 'Рекомендация: ' + info['recommendationKey']
    except KeyError:
        recs = ''
    buf = io.BytesIO()
    plt.savefig(buf, dpi=300)
    buf.seek(0)
    im = Image.open(buf)
    plt.clf()
    return [name + ': ' + comp + ' ' + str(market_price) + ' ' + currency + recs, im]
