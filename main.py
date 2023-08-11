from deribit import DeribitAPI
from deribit import Option, DeribitPortfolio

def main():
    api_key = '0KAFcKks' # "YOUR_API_KEY"
    api_secret = 'MTviEm1EAYUhmOq9MFx6gBXuYiTifgJ82lpKTMLQiOQ' # "YOUR_API_SECRET"

    deribit = DeribitAPI(api_key, api_secret)

    instruments = deribit.get_instruments()
    print("Instruments:", instruments)

    instrument_name = "BTC-PERPETUAL"
    orderbook = deribit.get_orderbook(instrument_name)
    print(f"Order book for {instrument_name}:", orderbook)


    # Crear instancias de opciones
    option1 = Option(symbol="BTC-28JAN22-50000-C", option_type="call", strike_price=50000, quantity=2)
    option2 = Option(symbol="BTC-28JAN22-45000-P", option_type="put", strike_price=45000, quantity=1)

    # Crear una instancia del portfolio
    portfolio = DeribitPortfolio()

    # Agregar las opciones al portfolio
    portfolio.add_option(option1)
    portfolio.add_option(option2)

    # Obtener el precio subyacente actual (debe reemplazarse con la obtención real)
    underlying_price = 47000

    # Calcular y mostrar el valor total del portfolio
    portfolio_value = portfolio.calculate_portfolio_value(underlying_price)
    print("Portfolio value:", portfolio_value)

if __name__ == "__main__":
    main()
