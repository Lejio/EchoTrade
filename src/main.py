from dotenv import dotenv_values
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, OrderType, TimeInForce
from alpaca.data.live.stock import StockDataStream

env = dotenv_values("../.env")

tclient = TradingClient(env["ALPACA_KEY"], env["ALPACA_SECRET"], paper=True)

account = tclient.get_account()

print(account)

# wss_client = StockDataStream(env["ALPACA_KEY"], env["ALPACA_SECRET"])

# async def data_handler(data):
#     print(data)
    
# wss_client.subscribe_quotes(data_handler, "")

# wss_client.run()

req = MarketOrderRequest(
    symbol="AAPL", 
    qty=1, 
    side=OrderSide.BUY, 
    type=OrderType.MARKET, 
    time_in_force=TimeInForce.DAY)

res = tclient.submit_order(req)

print(req)
