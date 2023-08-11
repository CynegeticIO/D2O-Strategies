import requests
import ccxt

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

class Deribit:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://www.deribit.com/api/v2/"

    def _make_request(self, endpoint, params=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        response = requests.get(self.base_url + endpoint, params=params, headers=headers)
        response_data = response.json()
        return response_data

    def get_instruments(self):
        endpoint = "public/get_instruments"
        return self._make_request(endpoint)

    def get_orderbook(self, instrument_name, depth=10):
        endpoint = "public/get_order_book"
        params = {
            "instrument_name": instrument_name,
            "depth": depth,
        }
        return self._make_request(endpoint, params=params)

class Option:
    def __init__(self, symbol, option_type, strike_price, quantity):
        self.symbol = symbol
        self.option_type = option_type
        self.strike_price = strike_price
        self.quantity = quantity

class DeribitPortfolio:
    def __init__(self):
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def calculate_portfolio_value(self, underlying_price):
        total_value = 0
        for option in self.options:
            option_value = 0
            if option.option_type == "call":
                option_value = max(underlying_price - option.strike_price, 0) * option.quantity
            elif option.option_type == "put":
                option_value = max(option.strike_price - underlying_price, 0) * option.quantity
            total_value += option_value
        return total_value


class DeribitConnector:
 
    def __init__(self, api_key=None, secret=None):
        self.exchange = ccxt.deribit({
            'apiKey': api_key,
            'secret': secret,
        })

    def fetch_option_instruments(self):
        # Obtener la lista de instrumentos de opciones disponibles
        return self.exchange.publicGetGetInstruments()

    def fetch_option_ticker(self, instrument_name):
        # Obtener el ticker para un instrumento de opción específico
        return self.exchange.publicGetTicker({'instrument_name': instrument_name})

    def fetch_order_book(self, instrument_name):
        # Obtener el libro de órdenes para un instrumento de opción específico
        return self.exchange.publicGetGetOrderBook({'instrument_name': instrument_name})
