# mercadobitcoin

[![Join the chat at https://gitter.im/python-mercadobitcoin/Lobby](https://badges.gitter.im/python-mercadobitcoin/Lobby.svg)](https://gitter.im/python-mercadobitcoin/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/alfakini/python-mercadobitcoin.svg?branch=master)](https://travis-ci.org/alfakini/python-mercadobitcoin)
[![Code Climate](https://codeclimate.com/github/alfakini/python-mercadobitcoin/badges/gpa.svg)](https://codeclimate.com/github/alfakini/python-mercadobitcoin)
[![Test Coverage](https://codeclimate.com/github/alfakini/python-mercadobitcoin/badges/coverage.svg)](https://codeclimate.com/github/alfakini/python-mercadobitcoin/coverage)
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

* http://www.mercadobitcoin.com.br/api/
* http://www.mercadobitcoin.com.br/tapi/configuracoes/#tab2
