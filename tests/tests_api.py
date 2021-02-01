import tests
import unittest
import mercadobitcoin


def assert_ticker_response(response):
    assert 'ticker' in response
    ticker_fields = {"high", "date", "sell", "vol", "last", "low", "buy"}
    for field in ticker_fields:
        assert field in response["ticker"]


def assert_trades_response(response):
    trade_fields = {"date", "price", "amount", "tid", "type"}
    for field in trade_fields:
        assert field in response[0]


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = mercadobitcoin.Api()


    @tests.vcr.use_cassette
    def test_ticker(self):
        response = self.api.ticker()
        assert_ticker_response(response)


    @tests.vcr.use_cassette
    def test_orderbook(self):
        response = self.api.orderbook()
        assert 'asks' in response
        assert 'bids' in response
        assert len(response['asks']) > 0
        assert len(response['bids']) > 0
        assert len(response['asks'][0]) == 2
        assert len(response['bids'][0]) == 2


    @tests.vcr.use_cassette
    def test_trades(self):
        response = self.api.trades()
        assert_trades_response(response)

    @tests.vcr.use_cassette
    def test_day_summary(self):
        response = self.api.day_summary(2013, 6, 12)
        summary_fields = {"date", "opening", "closing", "lowest", "highest",
                          "volume", "quantity", "amount", "avg_price"}
        for field in summary_fields:
            assert field in response


    @tests.vcr.use_cassette
    def test_ticker_litecoin(self):
        response = self.api.ticker_litecoin()
        assert_ticker_response(response)


    @tests.vcr.use_cassette
    def test_orderbook_litecoin(self):
        response = self.api.orderbook_litecoin()
        assert 'asks' in response
        assert 'bids' in response
        assert len(response['asks']) > 0
        assert len(response['bids']) > 0
        assert len(response['asks'][0]) == 2
        assert len(response['bids'][0]) == 2


    @tests.vcr.use_cassette
    def test_trades_litecoin(self):
        response = self.api.trades_litecoin()
        assert_trades_response(response)

