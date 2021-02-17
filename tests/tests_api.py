import tests
import unittest
import mercadobitcoin


def assert_ticker_response(response):
    assert 'ticker' in response
    ticker_fields = {"high", "date", "sell", "vol", "last", "low", "buy"}
    for field in ticker_fields:
        assert field in response["ticker"]

def assert_orderbook_response(response):
    assert 'asks' in response
    assert 'bids' in response
    assert len(response['asks']) > 0
    assert len(response['bids']) > 0
    assert len(response['asks'][0]) == 2
    assert len(response['bids'][0]) == 2

def assert_trades_response(response):
    assert len(response) > 0
    trade_fields = {"date", "price", "amount", "tid", "type"}
    for field in trade_fields:
        assert field in response[0]

def assert_summary_fields(response):
    summary_fields = {"date", "opening", "closing", "lowest", "highest",
                        "volume", "quantity", "amount", "avg_price"}
    for field in summary_fields:
        assert field in response


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
        assert_orderbook_response(response)

    @tests.vcr.use_cassette
    def test_orderbook_ethereum(self):
        response = self.api.orderbook(coin='ETH')
        assert_orderbook_response(response)

    @tests.vcr.use_cassette
    def test_trades(self):
        response = self.api.trades()
        assert_trades_response(response)

    @tests.vcr.use_cassette
    def test_trades_ethereum(self):
        response = self.api.trades(coin='ETH')
        assert_trades_response(response)

    @tests.vcr.use_cassette
    def test_trades_chainlink_from_date_to_date(self):
        min_date = 1612545400
        max_date = 1612545424
        response = self.api.trades(coin='LINK', from_date=min_date,
                                   to_date=max_date)
        assert_trades_response(response)
        assert len(response) > 1
        assert response[0]['date'] == min_date
        assert response[-1]['date'] == max_date
        for trade in response[1:-1]:
            assert trade['date'] > min_date
            assert trade['date'] < max_date

    @tests.vcr.use_cassette
    def test_trades_bitcoin_cash_tid(self):
        tid_threshold = 1616116
        response = self.api.trades(coin='BCH', tid=tid_threshold)
        assert_trades_response(response)
        assert response[0]['tid'] == tid_threshold + 1
        for trade in response:
            assert trade['tid'] > tid_threshold

    @tests.vcr.use_cassette
    def test_trades_bitcoin_cash_since(self):
        tid_threshold = 1616116
        response = self.api.trades(coin='BCH', since=tid_threshold)
        assert_trades_response(response)
        assert response[0]['tid'] == tid_threshold + 1
        for trade in response:
            assert trade['tid'] > tid_threshold

    @tests.vcr.use_cassette
    def test_trades_litecoin(self):
        response = self.api.trades_litecoin()
        assert_trades_response(response)

    @tests.vcr.use_cassette
    def test_day_summary(self):
        response = self.api.day_summary(year=2013, month=6, day=12)
        assert_summary_fields(response)

    @tests.vcr.use_cassette
    def test_day_summary_litecoin(self):
        response = self.api.day_summary(year=2013, month=8, day=23, coin='LTC')
        assert_summary_fields(response)

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


