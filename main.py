from deribit import DeribitAPI

def main():
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    deribit = DeribitAPI(api_key, api_secret)

    instruments = deribit.get_instruments()
    print("Instruments:", instruments)

    instrument_name = "BTC-PERPETUAL"
    orderbook = deribit.get_orderbook(instrument_name)
    print(f"Order book for {instrument_name}:", orderbook)

if __name__ == "__main__":
    main()
