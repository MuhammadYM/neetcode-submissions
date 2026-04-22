class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit  = sellPrice - buyPrice
        maxProfit = 0

        # while l < r:
        #     profit = prices[r] - prices[l]
        #     maxProfit = max(profit, maxProfit)

        for i, buyPrice in enumerate(prices):
            sellPrice = len(prices) - 1

            while i < sellPrice:
               profit = prices[sellPrice] - buyPrice
               maxProfit = max(profit, maxProfit) 
               sellPrice -=1
            
        return maxProfit


        