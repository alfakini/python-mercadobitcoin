python-mercadobitcoin
=====================

[![Join the chat at https://gitter.im/python-mercadobitcoin/Lobby](https://badges.gitter.im/python-mercadobitcoin/Lobby.svg)](https://gitter.im/python-mercadobitcoin/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A Python wrapper for Mercado Bitcoin API

```
mbtc = MercadoBitcoin()
mbtc.ticker()
mbtc.orderbook()
mbtc.trades()
mbtc.ticker_litecoin()
mbtc.orderbook_litecoin()
mbtc.trades_litecoin()
mbtc.info()
```

```
mbtc = MercadoBitcoin(api_key, api_code, pin)

mbtc.order_list({
    'pair': 'btc_brl',
    'type': 'buy',
    'status': 'active'
}) # pair, type, status, from_id, end_id, since

mbtc.trade({
    'pair': 'btc_brl',
    'type': 'buy',
    'volume': 3.4,
    'price': 2300.99
}) # pair, type, volume, price

mbtc.cancel_order({
    'pair': 'btc_brl',
    'order_id': 42
}) # pair, order_id
```

* http://www.mercadobitcoin.com.br/api/
* http://www.mercadobitcoin.com.br/tapi/configuracoes/#tab2
