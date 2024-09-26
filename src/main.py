from dotenv import dotenv_values
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, OrderType, TimeInForce
from alpaca.data.live.stock import StockDataStream

env = dotenv_values("../.env")

tclient = TradingClient(env["ALPACA_KEY"], env["ALPACA_SECRET"], paper=True)

account = tclient.get_account()

print(account)

stock_stream = StockDataStream(env["ALPACA_KEY"], env["ALPACA_SECRET"])

async def stock_data_stream_handler(data):
    print(data)
    
stock_stream.subscribe_quotes(stock_data_stream_handler, "AAPL")

stock_stream.run()

# req = MarketOrderRequest(
#     symbol="AAPL", 
#     qty=1, 
#     side=OrderSide.BUY, 
#     type=OrderType.MARKET, 
#     time_in_force=TimeInForce.DAY)

# res = tclient.submit_order(req)

# print(req)
