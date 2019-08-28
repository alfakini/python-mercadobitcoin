import os
from mercadobitcoin import TradeApi
import mercadobitcoin

mbtcPublic = mercadobitcoin.Api()
mbtcPrivate = TradeApi(os.getenv("API_ID"), bytes(os.getenv("API_SECRET"), 'latin1'))
#print(mbtcPrivate.get_account_info())
print('---------------------------------------')
print(mbtcPublic.ticker_ripple())


