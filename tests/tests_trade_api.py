import tests
import unittest
import mercadobitcoin
from mercadobitcoin.errors import ApiError, ArgumentError


def assert_order_response(response):
    assert "order" in response
    order_fields = {"status", "created_timestamp", "updated_timestamp",
                    "coin_pair", "has_fills", "quantity", "executed_quantity",
                    "order_id", "operations", "order_type",
                    "executed_price_avg", "fee", "limit_price"}
    for field in order_fields:
        assert field in response["order"]


def assert_withdrawal_response(response):
    assert "withdrawal" in response
    withdrawal_fields = {"id", "coin", "fee", "status", "description",
                         "created_timestamp", "updated_timestamp", "quantity"}
    for field in withdrawal_fields:
        assert field in response["withdrawal"]


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
        tradeable_coins = {"acmft", "acordo01", "asrft", "atmft", "bch", "brl",
            "btc", "caift", "chz", "eth", "galft", "imob01", "juvft", "link",
            "ltc", "mbcons01", "mbcons02", "mbfp01", "mbfp02", "mbprk01",
            "mbprk02", "mbprk03", "mbprk04", "mbvasco01", "mco2", "ogft",
            "paxg", "psgft", "usdc", "wbx", "xrp"}
        for coin in tradeable_coins:
            assert coin in response["balance"]
        for coin in response["balance"]:
            assert coin in tradeable_coins

        assert "withdrawal_limits" in response
        withdrawable_coins = {"brl", "btc", "ltc", "bch", "xrp", "eth"}
        for coin in withdrawable_coins:
            assert coin in response["withdrawal_limits"]
        for coin in response["withdrawal_limits"]:
            assert coin in withdrawable_coins


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
    def test_place_buy_order_with_invalid_quantity(self):
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
    def test_place_market_buy_order(self):
        response = self.api.place_market_buy_order(coin_pair="BRLBTC", cost="42.00")
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_place_market_sell_order(self):
        response = self.api.place_market_sell_order(coin_pair="BRLBTC", quantity="0.001")
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_cancel_order(self):
        response = self.api.cancel_order(coin_pair="BRLBTC", order_id=1)
        assert_order_response(response)


    @tests.vcr.use_cassette
    def test_get_brl_withdrawal(self):
        response = self.api.get_withdrawal(coin="BRL", withdrawal_id=42)
        assert_withdrawal_response(response)
        assert "net_quantity" in response["withdrawal"]
        assert "account" in response["withdrawal"]


    @tests.vcr.use_cassette
    def test_get_crypto_withdrawal(self):
        response = self.api.get_withdrawal(coin="BTC", withdrawal_id=42)
        assert_withdrawal_response(response)
        assert "address" in response["withdrawal"]
        assert "tx" in response["withdrawal"]


    # @tests.vcr.use_cassette
    # def test_get_xrp_withdrawal(self):
    #     response = self.api.get_withdrawal(coin="XRP", withdrawal_id=42)
    #     assert_withdrawal_response(response)
    #     assert "address" in response["withdrawal"]
    #     assert "tx" in response["withdrawal"]
    #     assert "destination_tag" in response["withdrawal"]


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
