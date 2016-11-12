# mercadobitcoin

[![Join the chat at https://gitter.im/python-mercadobitcoin/Lobby](https://badges.gitter.im/python-mercadobitcoin/Lobby.svg)](https://gitter.im/python-mercadobitcoin/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/alfakini/python-mercadobitcoin.svg?branch=master)](https://travis-ci.org/alfakini/python-mercadobitcoin)

A Python wrapper for Mercado Bitcoin API.

## Installation

Directly from [PyPI](https://pypi.python.org/pypi/mercadobitcoin):

```bash
pip install mercadobitcoin
```

You can also install directly from the GitHub repository to have the newest features by running:

```bash
git clone https://github.com/alfakini/python-mercadobitcoin.git
cd python-mercadobitcoin
python setup.py install
```

## Basic Usage

```python
from mercadobitcoin import MercadoBitcoin

mbtc = MercadoBitcoin()
mbtc.ticker()
mbtc.orderbook()
mbtc.trades()
mbtc.ticker_litecoin()
mbtc.orderbook_litecoin()
mbtc.trades_litecoin()
mbtc.info()
```

```python
from mercadobitcoin import MercadoBitcoin

mbtc = MercadoBitcoin(<API_KEY>, <API_CODE>, <PIN>)

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

## Development

Install development dependencies:

```bash
pip install -r requirements-development.txt
```

Run tests:

```bash
tox
```

## References

* http://www.mercadobitcoin.com.br/api/
* http://www.mercadobitcoin.com.br/tapi/configuracoes/#tab2
