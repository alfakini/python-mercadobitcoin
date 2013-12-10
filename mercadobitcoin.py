import urllib
import urllib2
import httplib
import json
import time
import hashlib
import hmac
import itertools

__author__ = "alf."
__version__ = "0.1"

def check_required(params, required):
    for param in required:
        if param not in params:
            raise MercadoBitcoinError(u'Parameter %s is required' % param)

def check_values(defaults, options):
    keys = itertools.chain(options.keys())
    for param, value in defaults.items():
        if param not in keys:
            continue
        if value not in options[param]:
            raise MercadoBitcoinError(u'Valor do %s invalido' % param)

class MercadoBitcoinError(Exception):
    def __init__(self, error):
        self.error =error

    def __str__(self):
        return repr(self.error)

class MercadoBitcoin(object):
    def __init__(self, key=None, code=None, pin=None):
        self.base_url = "www.mercadobitcoin.com.br"
        self.key = key
        self.code = code
        self.pin = str(pin)

    def ticker(self):
        return self.__get_api('ticker')

    def orderbook(self):
        return self.__get_api('orderbook')

    def trades(self):
        return self.__get_api('trades')

    def ticker_litecoin(self):
        return self.__get_api('ticker_litecoin')

    def orderbook_litecoin(self):
        return self.__get_api('orderbook_litecoin')

    def trades_litecoin(self):
        return self.__get_api('trades_litecoin')

    def info(self):
        return self.__check_response(self.__post_tapi('getInfo'))

    def order_list(self, params={}):
        defaults = {
            'pair': 'btc_brl'
        }
        defaults.update(params)
        check_required(defaults.keys(), ['pair'])
        check_values(defaults, {
            'pair': ['btc_brl', 'ltc_brl'],
            'type': ['buy', 'sell'],
            'status': ['active', 'canceled', 'completed']
        })

        return self.__check_response(self.__post_tapi('OrderList', defaults))

    def trade(self, params={}):
        defaults = {
            'pair': 'btc_brl'
        }
        defaults.update(params)

        check_required(defaults.keys(), ['pair', 'type', 'volume', 'price'])
        check_values(defaults, {
            'pair': ['btc_brl', 'ltc_brl'],
            'type': ['buy', 'sell'],
        })

        return self.__check_response(self.__post_tapi('Trade', defaults))

    def cancel_order(self, params={}):
        defaults = {
            'pair': 'btc_brl'
        }
        defaults.update(params)

        check_required(defaults.keys(), ['pair', 'order_id'])
        check_values(defaults, {
            'pair': ['btc_brl', 'ltc_brl'],
        })

        return self.__check_response(self.__post_tapi('CancelOrder', defaults))

    def __check_response(self, response):
        if response['success'] == 1:
            return response
        else:
            raise MercadoBitcoinError(response['error'])

    def __get_api(self, action):
        return json.load(urllib2.urlopen("%s/api/%s" % (self.base_url, action)))

    def __post_tapi(self, method, params={}):
        defaults = {
            'method': method,
            'tonce': str(int(time.time()))
        }
        defaults.update(params)

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Key": self.key,
            "Sign": self.__signature(method, defaults['tonce'])
        }

        conn = httplib.HTTPSConnection(self.base_url)
        conn.request("POST", "/tapi/", urllib.urlencode(defaults), headers)

        response = conn.getresponse()
        conn.close()

        return json.load(response)

    def __signature(self, method, tonce):
        signature = hmac.new(self.code, digestmod=hashlib.sha512)
        signature.update(method + ':' + self.pin + ':' + tonce)
        return signature.hexdigest()



