from buy_sell_stk_once import buy_sell_stock_once
from alternation import alternation


def test_sell_once():
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    assert buy_sell_stock_once(prices) == 30, "Max profit should be 30"


def test_alternation():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    assert alternation(numbers) == [1, 3, 2, 5, 4, 7, 6]
