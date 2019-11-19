def buy_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    
    for price in prices:
        max_profit_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_today)
        min_price_so_far = min(price, min_price_so_far)
    
    return max_profit
