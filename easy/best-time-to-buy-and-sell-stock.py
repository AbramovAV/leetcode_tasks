class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_sum = 0
        buying_price = prices[0]
        for price in prices[1:]:
            if price<buying_price:
                buying_price = price
            elif price > buying_price:
                best_sum = max(best_sum, price-buying_price)
        return best_sum