import requests

class DeribitAPI:
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
