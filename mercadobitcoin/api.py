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

    def ticker(self):
        """Return information about Bitcoin market."""
        return self.get_api('ticker')


    def orderbook(self):
        """Return Bitcoin's orderbook."""
        return self.get_api('orderbook')


    def trades(self):
        """Return the operation list for the Bitcoin market."""
        return self.get_api('trades')


    def ticker_litecoin(self):
        """Return information about Litecoin market."""
        return self.get_api('ticker_litecoin')


    def ticker_ripple(self):
        """Return information about Ripple market."""
        return self.get_api('xrp/ticker')


    def orderbook_litecoin(self):
        """Return Litecoin's orderbook."""
        return self.get_api('orderbook_litecoin')


    def trades_litecoin(self):
        """Return the operation list for the Litecoin market."""
        return self.get_api('trades_litecoin')
