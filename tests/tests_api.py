import tests
import unittest
import mercadobitcoin


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = mercadobitcoin.Api()


    @tests.vcr.use_cassette
    def test_ticker(self):
        response = self.api.ticker()
        assert 'ticker' in response
        assert 'high' in response['ticker']
        assert 'date' in response['ticker']
        assert 'sell' in response['ticker']
        assert 'vol' in response['ticker']
        assert 'last' in response['ticker']
        assert 'low' in response['ticker']
        assert 'buy' in response['ticker']


    @tests.vcr.use_cassette
    def test_orderbook(self):
        response = self.api.orderbook()
        assert 'asks' in response
        assert 'bids' in response
        assert len(response['asks']) > 0
        assert len(response['bids']) > 0


    @tests.vcr.use_cassette
    def test_trades(self):
        response = self.api.trades()
        assert 'date' in response[0]
        assert 'price' in response[0]
        assert 'amount' in response[0]
        assert 'tid' in response[0]
        assert 'type' in response[0]


    @tests.vcr.use_cassette
    def test_ticker_litecoin(self):
        response = self.api.ticker_litecoin()
        assert 'ticker' in response
        assert 'high' in response['ticker']
        assert 'date' in response['ticker']
        assert 'sell' in response['ticker']
        assert 'vol' in response['ticker']
        assert 'last' in response['ticker']
        assert 'low' in response['ticker']
        assert 'buy' in response['ticker']


    @tests.vcr.use_cassette
    def test_orderbook_litecoin(self):
        response = self.api.orderbook_litecoin()
        assert 'asks' in response
        assert 'bids' in response
        assert len(response['asks']) > 0
        assert len(response['bids']) > 0


    @tests.vcr.use_cassette
    def test_trades_litecoin(self):
        response = self.api.trades_litecoin()
        assert 'date' in response[0]
        assert 'price' in response[0]
        assert 'amount' in response[0]
        assert 'tid' in response[0]
        assert 'type' in response[0]

