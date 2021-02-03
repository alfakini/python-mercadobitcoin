import requests


class Base(object):
    """Base API Class"""

    def __init__(self):
        self.host = "www.mercadobitcoin.net"

    def get_api(self, action):
        """Return api JSON for the requested action.

        param action: The requested API action
        """
        response = requests.get("https://%s/api/%s/" % (self.host, action))
        return response.json()


class Api(Base):
    """Market information for each cryptoasset."""

    def ticker(self, coin='BTC'):
        """Return information about Bitcoin market."""
        return self.get_api('{}/ticker'.format(coin))

    def orderbook(self, coin='BTC'):
        """Return Bitcoin's orderbook."""
        return self.get_api('{}/orderbook'.format(coin))

    def trades(self, coin='BTC'):
        """Return the operation list for the Bitcoin market."""
        return self.get_api('{}/trades'.format(coin))

    def day_summary(self, year, month, day, coin='BTC'):
        """Return a summary of the BTC trades for the specified date."""
        return self.get_api('{}/day-summary/{}/{}/{}'.format(coin, year, month, day))

    def ticker_litecoin(self):
        """Return information about Litecoin market."""
        return self.ticker(coin='LTC')

    def ticker_ripple(self):
        """Return information about Ripple market."""
        return self.ticker(coin='XRP')

    def orderbook_litecoin(self):
        """Return Litecoin's orderbook."""
        return self.orderbook(coin='LTC')

    def trades_litecoin(self, coin='LTC'):
        """Return the operation list for the Litecoin market."""
        return self.trades(coin='LTC')
