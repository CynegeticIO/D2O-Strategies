import requests
import ccxt
import matplotlib.pyplot as plt

class DeribitAPI:
    def __init__(self):
        self.exchange = ccxt.deribit({
            'apiKey': '0KAFcKks',
            'secret': 'MTviEm1EAYUhmOq9MFx6gBXuYiTifgJ82lpKTMLQiOQ',
        })

    def fetch_option_instruments(self):
        params = {'currency': 'BTC'}  # Cambiar a 'ETH' si deseas instrumentos de Ethereum
        return self.exchange.publicGetGetInstruments(params=params)

    def fetch_ticker(self, symbol):
        return self.exchange.publicGetTicker({'instrument_name': symbol})

    def fetch_order_book(self, symbol):
        return self.exchange.publicGetGetOrderBook({'instrument_name': symbol})

class DeribitDraw:

    def __init__(self):
        self.exchange = ccxt.deribit({
            'rateLimit': 6000,
            'enableRateLimit': True,
        })
    
    def fetch_option_prices(self, symbol):
        return self.exchange.fetch_ticker(symbol)
    
    def plot_option_prices(self, option_prices):
        last_price = option_prices['last']
        bid_price = option_prices['bid']
        ask_price = option_prices['ask']

        plt.figure(figsize=(10, 6))
        plt.plot(['Last', 'Bid', 'Ask'], [last_price, bid_price, ask_price], marker='o')
        plt.ylabel('Price')
        plt.title('Option Prices')
        plt.show()
