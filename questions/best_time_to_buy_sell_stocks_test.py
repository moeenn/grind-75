from unittest import TestCase

from .best_time_to_buy_sell_stocks import best_time_to_buy_sell_stocks


class TestBestTimeToBuySellStocks(TestCase):
    def test_profit_scenario(self) -> None:
        profit = best_time_to_buy_sell_stocks([7, 1, 5, 3, 6, 4])
        self.assertEqual(profit, 5)

    def test_loss_scenario(self) -> None:
        profit = best_time_to_buy_sell_stocks([7, 6, 4, 3, 1])
        self.assertEqual(profit, 0)
