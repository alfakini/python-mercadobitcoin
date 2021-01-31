import tests
import unittest
import mercadobitcoin
from mercadobitcoin.errors import ApiError, ArgumentError


def assert_order_response(response):
    assert "order" in response
    assert "status" in response["order"]
    assert "created_timestamp" in response["order"]
    assert "updated_timestamp" in response["order"]
    assert "coin_pair" in response["order"]
    assert "has_fills" in response["order"]
    assert "quantity" in response["order"]
    assert "executed_quantity" in response["order"]
    assert "order_id" in response["order"]
    assert "operations" in response["order"]
    assert "order_type" in response["order"]
    assert "executed_price_avg" in response["order"]
    assert "fee" in response["order"]
    assert "limit_price" in response["order"]


class TradeApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = mercadobitcoin.TradeApi(b"42", b"42")


    @tests.vcr.use_cassette
    def test_list_system_messages(self):
        response = self.api.list_system_messages()
        assert "messages" in response


    @tests.vcr.use_cassette
    def test_get_account_info(self):
        response = self.api.get_account_info()
        assert "balance" in response
        assert "brl" in response["balance"]
        assert "btc" in response["balance"]
        assert "ltc" in response["balance"]
        assert "withdrawal_limits" in response
        assert "brl" in response["withdrawal_limits"]
        assert "btc" in response["withdrawal_limits"]
        assert "ltc" in response["withdrawal_limits"]


    @tests.vcr.use_cassette
    def test_get_order(self):
        response = self.api.get_order(coin_pair="BRLBTC", order_id=42)
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_get_order_with_invalid_order_id(self):
        with self.assertRaises(ApiError):
            self.api.get_order(coin_pair="BRLBTC", order_id=0)


    @tests.vcr.use_cassette
    def test_list_orders(self):
        response = self.api.list_orders(coin_pair="BRLBTC")
        assert len(response["orders"]) > 0


    @tests.vcr.use_cassette
    def test_list_orderbook(self):
        response = self.api.list_orderbook(coin_pair="BRLBTC")
        assert "orderbook" in response
        assert "latest_order_id" in response["orderbook"]
        assert len(response["orderbook"]["bids"]) > 0
        assert len(response["orderbook"]["asks"]) > 0


    @tests.vcr.use_cassette
    def test_place_buy_order(self):
        response = self.api.place_buy_order(coin_pair="BRLBTC", quantity="42.00", limit_price="5000")
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_place_buy_order_with_invalid_quatity(self):
        with self.assertRaises(ArgumentError):
            self.api.place_buy_order(coin_pair="BRLBTC", quantity=1, limit_price="42")


    @tests.vcr.use_cassette
    def test_place_sell_order(self):
        response = self.api.place_sell_order(coin_pair="BRLBTC", quantity="42.000", limit_price="5000.00")
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_place_sell_order_with_invalid_quantity(self):
        with self.assertRaises(ApiError):
            self.api.place_sell_order(coin_pair="BRLBTC", quantity="0.00001", limit_price="5000")


    @tests.vcr.use_cassette
    def test_cancel_order(self):
        response = self.api.cancel_order(coin_pair="BRLBTC", order_id=1)
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_withdraw_coin_brl_untrusted_account(self):
        with self.assertRaises(ApiError):
            self.api.withdraw_coin_brl(coin="BRL", quantity="4200.00", account_ref="1234567")


    @tests.vcr.use_cassette
    def test_withdraw_coin_untrusted_address(self):
        with self.assertRaises(ApiError):
            self.api.withdraw_coin(coin="BTC", quantity="9999999", address="random81XF3WPnLEXzSYh9yDrZqGKOzxxP", tx_fee=" 0.0004", description="Trasfering Crypto.")


    @tests.vcr.use_cassette
    def test_withdraw_coin_xrp_invalid_address(self):
        with self.assertRaises(ApiError):
            self.api.withdraw_coin_xrp(coin="XRP", quantity="42", address="1", tx_fee="0.01", destination_tag=123456789, description="Trasfering XRP.")
