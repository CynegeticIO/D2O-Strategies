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
