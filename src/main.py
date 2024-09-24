from dotenv import dotenv_values
from alpaca.trading.client import TradingClient

env = dotenv_values("../.env")

tclient = TradingClient(env["ALPACA_KEY"], env["ALPACA_SECRET"], paper=True)

account = tclient.get_account()

print(account)


