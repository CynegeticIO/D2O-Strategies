from deribit import DeribitAPI
import pandas as pd


def main():

    deribit = DeribitAPI()

    option_instruments = deribit.fetch_option_instruments()
    # print("Option Instruments:", option_instruments)

    btc_ticker = deribit.fetch_ticker('BTC-PERPETUAL')
    # print("BTC Ticker:", btc_ticker)

    eth_order_book = deribit.fetch_order_book('ETH-PERPETUAL')
    # print("ETH Order Book:", eth_order_book)

    # Convertir el resultado JSON en una tabla (DataFrame)
    df_op = pd.DataFrame(option_instruments['result'])
    df_btc = pd.DataFrame(btc_ticker['result'])
    print("Option Instruments Table:")
    print(df_btc)


if __name__ == "__main__":
    main()
