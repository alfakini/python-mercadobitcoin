import requests

from .validation import check_args


class Base(object):
    """Base API Class"""

    def __init__(self):
        self.host = "www.mercadobitcoin.net"

    def get_api(self, action, params=None):
        """Return api JSON for the requested action.

        param action: The requested API action
        """
        response = requests.get(
            "https://%s/api/%s/" % (self.host, action),
            params=params
        )
        return response.json()


class Api(Base):
    """Market information for each cryptoasset."""

    def __init__(self):
        self.available_coins = [
            "ACMFT", "ACORDO01", "ASRFT", "ATMFT", "BCH", "BTC", "CAIFT",
            "CHZ", "ETH", "GALFT", "IMOB01", "JUVFT", "LINK", "LTC",
            "MBCONS01", "MBCONS02", "MBFP01", "MBFP02", "MBPRK01", "MBPRK02",
            "MBPRK03", "MBPRK04", "MBVASCO01", "MCO2", "OGFT", "PAXG", "PSGFT",
            "USDC", "WBX", "XRP"
        ]
        self.available_methods = [
            "ticker", "orderbook", "trades", "day-summary"
        ]
        Base.__init__(self)

    def ticker(self, coin="BTC"):
        """Return information about Bitcoin market."""
        return self.__get_api(coin, "ticker")

    def orderbook(self, coin="BTC"):
        """Return Bitcoin's orderbook."""
        return self.__get_api(coin, "orderbook")

    def trades(self, coin="BTC", **kwargs):
        """Return the operation list for the Bitcoin market."""
        check_args(
            kwargs,
            {},
            {"tid": int, "since": int, "from_date": int, "to_date": int}
        )
        path=None
        if "from_date" in kwargs:
            path = kwargs["from_date"]
            if "to_date" in kwargs:
                path = "{}/{}".format(path, kwargs["to_date"])
        params={}
        if "tid" in kwargs:
            params.update({"tid": kwargs["tid"]})
        if "since" in kwargs:
            params.update({"since": kwargs["since"]})
        return self.__get_api(coin, "trades", path=path, params=params)

    def day_summary(self, coin="BTC", **kwargs):
        """Return a summary of the BTC trades for the specified date."""
        check_args(kwargs, {"year": int, "month": int, "day": int})
        path = "{}/{}/{}".format(kwargs["year"], kwargs["month"],
                                 kwargs["day"])
        return self.__get_api(coin, "day-summary", path=path)

    def ticker_litecoin(self):
        """Return information about Litecoin market."""
        return self.ticker(coin="LTC")

    def ticker_ripple(self):
        """Return information about Ripple market."""
        return self.ticker(coin="XRP")

    def orderbook_litecoin(self):
        """Return Litecoin's orderbook."""
        return self.orderbook(coin="LTC")

    def trades_litecoin(self):
        """Return the operation list for the Litecoin market."""
        return self.trades(coin="LTC")

    def __get_api(self, coin, method, path=None, params=None):
        all_args = {"coin": coin, "method": method}
        check_args(all_args, {"coin": self.available_coins,
                              "method": self.available_methods})
        action = "{}/{}".format(coin, method)
        if path:
            action = "{}/{}".format(action, path)
        return self.get_api(action, params=params)
