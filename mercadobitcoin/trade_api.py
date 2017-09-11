import requests
import urllib
import time
import hashlib
import hmac
import itertools

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from .api import Base
from .errors import ApiError, ArgumentError

def check_values(value, arg, arg_value):
    if type(value) == type:
        if type(arg_value) != value:
            raise ArgumentError(u"Type of argument {} is invalid. It should be {}".format(arg, value))
    elif arg_value not in value:
        raise ArgumentError(u"Value of argument {} is invalid. It should be one of {}".format(arg, value))


def check_args(kwargs, required_parameters, optional_parameters={}):
    args = kwargs.keys()
    required_args = required_parameters.keys()
    optional_args = optional_parameters.keys()

    missing_args = list(set(required_args) - set(args))
    if len(missing_args) > 0:
        raise ArgumentError(u"Parameter {} is required".format(missing_args))

    for arg_name, arg_value in kwargs.items():
        if arg_name in optional_args:
            optional_value = optional_parameters[arg_name]
            check_values(optional_value, arg_name, arg_value)
        elif arg_name in required_args:
            required_value = required_parameters[arg_name]
            check_values(required_value, arg_name, arg_value)


class TradeApi(Base):
    def __init__(self, identifier=None, secret=None):
        self.id = identifier
        self.secret = secret
        self.path = "/tapi/v3/"
        Base.__init__(self)


    def list_system_messages(self, level="INFO"):
        """https://www.mercadobitcoin.com.br/trade-api/#list_system_messages"""

        payload = { "level": level }
        check_args(payload, { "level": ["INFO", "WARNING", "ERROR"] })
        return self.__check_response(self.__post_tapi("list_system_messages", payload))


    def get_account_info(self):
        """https://www.mercadobitcoin.com.br/trade-api/#get_account_info"""
        return self.__check_response(self.__post_tapi("get_account_info"))


    def get_order(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#get_order"""

        check_args(kwargs, { "coin_pair": ["BRLBTC", "BRLLTC", "BRLBCH"], "order_id": int })
        return self.__check_response(self.__post_tapi("get_order", kwargs))


    def list_orders(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#list_orders"""

        check_args(kwargs, { "coin_pair": ["BRLBTC", "BRLLTC", "BRLBCH"] }, { "order_type": [1, 2], "status_list": str, "has_fills": [True, False], "from_id": int, "to_id": int, "from_timestamp": str, "to_timestamp": str })
        return self.__check_response(self.__post_tapi("list_orders", kwargs ))


    def list_orderbook(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#list_orderbook"""

        check_args(kwargs, { "coin_pair": ["BRLBTC", "BRLLTC", "BRLBCH"] }, { "full": [True, False] })
        return self.__check_response(self.__post_tapi("list_orderbook", kwargs ))


    def place_buy_order(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#place_buy_order"""

        check_args(kwargs, { "coin_pair": ["BRLBTC", "BRLLTC", "BRLBCH"], "quantity": str, "limit_price": str })
        return self.__check_response(self.__post_tapi("place_buy_order", kwargs ))


    def place_sell_order(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#place_sell_order"""

        check_args(kwargs, { "coin_pair": ["BRLBTC", "BRLLTC", "BRLBCH"], "quantity": str, "limit_price": str })
        return self.__check_response(self.__post_tapi("place_sell_order", kwargs ))


    def cancel_order(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#cancel_order"""

        check_args(kwargs, { "coin_pair": ["BRLBTC", "BRLLTC", "BRLBCH"], "order_id": int })
        return self.__check_response(self.__post_tapi("cancel_order", kwargs ))


    def get_withdrawal(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#get_withdrawal"""

        check_args(kwargs, { "coin": ["BRL", "BTC", "LTC", "BCH"], "withdrawal_id": int })
        return self.__check_response(self.__post_tapi("get_withdrawal", kwargs ))


    def withdraw_coin(self, **kwargs):
        """https://www.mercadobitcoin.com.br/trade-api/#withdraw_coin"""

        check_args(kwargs, { "coin": ["BRL", "BTC", "LTC", "BCH"], "quantity": str, "destiny": str }, { "description": str })
        return self.__check_response(self.__post_tapi("withdraw_coin", kwargs ))


    def __check_response(self, response):
        if response["status_code"] == 100:
            return response["response_data"]
        else:
            raise ApiError(response["error_message"], response["status_code"])


    def __post_tapi(self, method, params={}):
        payload = { "tapi_method": method, "tapi_nonce": str(int(time.time()*1000000))}
        payload.update(params)

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "TAPI-ID": self.id,
            "TAPI-MAC": self.__signature(payload)
        }

        response = requests.post("https://{}{}".format(self.host, self.path), headers=headers, data=payload)
        return response.json()


    def __signature(self, payload):
        signature = hmac.new(self.secret, digestmod=hashlib.sha512)
        params = self.path + '?' + urlencode(payload)
        signature.update(params.encode('utf-8'))
        return signature.hexdigest()
