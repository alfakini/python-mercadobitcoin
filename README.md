# mercadobitcoin

[![Join the chat at https://gitter.im/python-mercadobitcoin/Lobby](https://badges.gitter.im/python-mercadobitcoin/Lobby.svg)](https://gitter.im/python-mercadobitcoin/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/alfakini/python-mercadobitcoin.svg?branch=master)](https://travis-ci.org/alfakini/python-mercadobitcoin)
[![PyPI](https://img.shields.io/pypi/v/mercadobitcoin.svg)](https://pypi.python.org/pypi/mercadobitcoin)

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

Below you can see the available Mercado Bitcoin API methods you can use:

```python
import mercadobitcoin
mbtc = mercadobitcoin.Api()
mbtc.ticker()
mbtc.orderbook()
mbtc.trades()
mbtc.ticker_litecoin()
mbtc.orderbook_litecoin()
mbtc.trades_litecoin()
```

And the private Trade API:

```python
from mercadobitcoin import TradeApi

mbtc = TradeApi(<API_ID>, <API_SECRET>)

mbtc.list_system_messages()
mbtc.get_account_info()
mbtc.get_order(coin_pair="BRLBTC", order_id=1)
mbtc.list_orders(coin_pair="BRLBTC")
mbtc.list_orderbook(coin_pair="BRLBTC")
mbtc.place_buy_order(coin_pair="BRLBTC", quantity="42.00", limit_price="5000")
mbtc.place_sell_order(coin_pair="BRLBTC", quantity="42.00", limit_price="5000")
mbtc.cancel_order(coin_pair="BRLBTC", order_id=1)
mbtc.get_withdrawal(coin="BRL", withdrawal_id=1)
mbtc.withdraw_coin(coin_pair="BRL", quantity="42", destiny="1", description="Trasfering Money.")
```

## Development

Install development dependencies:

```bash
brew install libyaml
pip install -r requirements-development.txt
```

Run tests:

```bash
tox
```

## References

* [Mercado Bitcoin public data API](https://www.mercadobitcoin.com.br/api-doc)
* [Mercado Bitcoin private trade API](https://www.mercadobitcoin.com.br/trade-api)
