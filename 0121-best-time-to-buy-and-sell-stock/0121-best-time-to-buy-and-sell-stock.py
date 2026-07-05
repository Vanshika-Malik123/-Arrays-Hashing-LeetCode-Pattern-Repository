class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Cheapest price seen so far
        min_price = prices[0]

        # Best profit found so far
        max_profit = 0

        # Traverse the array
        for price in prices:

            # Update the minimum price if a cheaper stock is found
            if price < min_price:
                min_price = price

            # Calculate profit if we sell today
            profit = price - min_price

            # Update the maximum profit
            max_profit = max(max_profit, profit)

        return max_profit


        