import requests

class Base(object):
    """Base API Class"""

    def __init__(self):
        self.host = "www.mercadobitcoin.net"


    def get_api(self, action):
        """Returns api json for requested action.

        param action: The requested API action
        """
        response = requests.get("https://%s/api/%s" % (self.host, action))
        return response.json()


class Api(Base):
    """Bitcoin and Litcoin market informations."""

    def ticker(self):
        """Returns informations about Bitcoin market."""
        return self.get_api('ticker')


    def orderbook(self):
        """Returns the Bitcoin's orderbook."""
        return self.get_api('orderbook')


    def trades(self):
        """Returns the operation list for the Bitcoin market."""
        return self.get_api('trades')


    def ticker_litecoin(self):
        """Return informations about Litcoin market."""
        return self.get_api('ticker_litecoin')


    def orderbook_litecoin(self):
        """Returns the Litecoin's orderbook."""
        return self.get_api('orderbook_litecoin')


    def trades_litecoin(self):
        """Returns the operation list for the Litcoin market."""
        return self.get_api('trades_litecoin')
