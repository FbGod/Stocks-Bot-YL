import yfinance as yf
import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse
from pprint import pprint


# Перевод валют с использованием xrates
def get_exchange_list_xrates(currency, amount=1):
    # make the request to x-rates.com to get current exchange rates for common currencies
    content = requests.get(f"https://www.x-rates.com/table/?from={currency}&amount={amount}").content
    # initialize beautifulsoup
    soup = bs(content, "html.parser")
    # get the last updated time
    price_datetime = parse(soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text)
    # get the exchange rates tables
    exchange_tables = soup.find_all("table")
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            # for each row in the table
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                # get the exchange rate
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate
    return price_datetime, exchange_rates


# Цена одной ценной бумаги в рублях на текущий момент
def get_one_price(currency, price):
    return get_exchange_list_xrates(currency, price)[1]['Russian Ruble']


# Общая цена портфеля
def total_cost(ticker_set):
    total_cost_value = 0
    for ticker, quantity in ticker_set:
        currency = yf.Ticker(ticker).info['currency']
        try:
            market_price = yf.Ticker(ticker).info['currentPrice']
        except KeyError:
            market_price = yf.Ticker(ticker).info['previousClose']
        if currency != 'RUB':
            price_datetime, exchange_rates = get_exchange_list_xrates(currency, market_price)
            market_price = exchange_rates['Russian Ruble']
        market_price = market_price * quantity
        total_cost_value += market_price
    return total_cost_value


# Информация по типу ценной бумаги
def type_ratio(ticker_set):
    types = {}
    for ticker, quantity in ticker_set:
        currency = yf.Ticker(ticker).info['currency']
        try:
            market_price = yf.Ticker(ticker).info['currentPrice']
            market_price_ish = yf.Ticker(ticker).info['currentPrice']
        except KeyError:
            market_price = yf.Ticker(ticker).info['previousClose']
            market_price_ish = yf.Ticker(ticker).info['previousClose']
        if currency != 'RUB':
            market_price = get_one_price(currency, market_price)
        market_price *= quantity
        market_price_ish *= quantity
        q_type = yf.Ticker(ticker).info['quoteType']
        types.setdefault(q_type, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                             [market_price, 'RUB']])
    return types


# Информация о компаниях, предоставляющих ценные бумаги
def companies_ratio(ticker_set):
    companies = {}
    for ticker, quantity in ticker_set:
        currency = yf.Ticker(ticker).info['currency']
        try:
            market_price = yf.Ticker(ticker).info['currentPrice']
            market_price_ish = yf.Ticker(ticker).info['currentPrice']
        except KeyError:
            market_price = yf.Ticker(ticker).info['previousClose']
            market_price_ish = yf.Ticker(ticker).info['previousClose']
        if currency != 'RUB':
            market_price = get_one_price(currency, market_price)
        market_price *= quantity
        market_price_ish *= quantity
        comp = yf.Ticker(ticker).info['shortName']
        companies.setdefault(comp, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                             [market_price, 'RUB']])
    return companies


# Информация об отраслях
def industries_ratio(ticker_set):
    industries = {}
    for ticker, quantity in ticker_set:
        currency = yf.Ticker(ticker).info['currency']
        try:
            market_price = yf.Ticker(ticker).info['currentPrice']
            market_price_ish = yf.Ticker(ticker).info['currentPrice']
        except KeyError:
            market_price = yf.Ticker(ticker).info['previousClose']
            market_price_ish = yf.Ticker(ticker).info['previousClose']
        if currency != 'RUB':
            market_price = get_one_price(currency, market_price)
        market_price *= quantity
        market_price_ish *= quantity
        try:
            comp = yf.Ticker(ticker).info['industry']
        except KeyError:
            comp = 'No type'
        industries.setdefault(comp, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                             [market_price, 'RUB']])
    return industries


# Валютное соотношение
def currency_ratio(ticker_set):
    industries = {}
    for ticker, quantity in ticker_set:
        currency = yf.Ticker(ticker).info['currency']
        try:
            market_price = yf.Ticker(ticker).info['currentPrice']
            market_price_ish = yf.Ticker(ticker).info['currentPrice']
        except KeyError:
            market_price = yf.Ticker(ticker).info['previousClose']
            market_price_ish = yf.Ticker(ticker).info['previousClose']
        if currency != 'RUB':
            market_price = get_one_price(currency, market_price)
        market_price *= quantity
        market_price_ish *= quantity
        try:
            comp = yf.Ticker(ticker).info['industry']
        except KeyError:
            comp = 'No type'
        industries.setdefault(comp, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                             [market_price, 'RUB']])
    return industries


def get_all_information(ticker_set):
    industries = {}
    companies = {}
    types = {}
    for ticker, quantity in ticker_set:
        currency = yf.Ticker(ticker).info['currency']
        try:
            market_price = yf.Ticker(ticker).info['currentPrice']
            market_price_ish = yf.Ticker(ticker).info['currentPrice']
        except KeyError:
            market_price = yf.Ticker(ticker).info['previousClose']
            market_price_ish = yf.Ticker(ticker).info['previousClose']
        if currency != 'RUB':
            market_price = get_one_price(currency, market_price)
        market_price *= quantity
        market_price_ish *= quantity
        try:
            comp = yf.Ticker(ticker).info['industry']
        except KeyError:
            comp = 'No type'
        industries.setdefault(comp, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                                [market_price, 'RUB']])
        comp = yf.Ticker(ticker).info['shortName']
        companies.setdefault(comp, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                               [market_price, 'RUB']])
        q_type = yf.Ticker(ticker).info['quoteType']
        types.setdefault(q_type, []).append([yf.Ticker(ticker).info['shortName'], [market_price_ish, currency],
                                             [market_price, 'RUB']])

    return [types, companies, industries]





# YNDX = yf.Ticker("YNDX.ME")
# print(YNDX.info)

# print(type_ratio([['YNDX.ME', 4], ['AAPL', 2], ['GC=F', 5]]))
# print(total_cost([['YNDX.ME', 4], ['AAPL', 2], ['GC=F', 5]]))
# print(industries_ratio([['YNDX.ME', 4], ['AAPL', 2], ['GC=F', 5]]))
# print(companies_ratio([['YNDX.ME', 4], ['AAPL', 2], ['GC=F', 5]]))
# print(get_all_information([['YNDX.ME', 4], ['AAPL', 2], ['GC=F', 5]]))
