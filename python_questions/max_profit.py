"""
Write a Python function called max_profit that takes a list of integers,
where the i-th integer represents the price of a given stock on day i,
and returns the maximum profit you can achieve by buying and selling the stock.

You may complete, at most, two complete buy/sell transactions to maximize profits on a stock.
"""
#%%
def max_profit(prices):

    if not prices:
        return 0

    buy1 = buy2 = -float('inf')
    sell1 = sell2 = 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, price + buy1)
        buy2 = max(buy2, sell1-price)
        sell2 = max(sell2, price + buy2)

    return sell2

#%%
# --- Main execution ---
if __name__ == "__main__":

    # Test cases for the max_profit function
    test1 = [3, 2, 6, 5, 0, 3]
    test2 = [3, 3, 5, 0, 0, 3, 1, 4]

    for test in [test1, test2]:
        result = max_profit(test)
        print(f"Maximum profit for prices {test} is: {result}")

print("== Code Execution Complete ==")
