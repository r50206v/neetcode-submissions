class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = float("-Inf")
        buyInPrice = prices[0]
        for idx in range(len(prices)):
            if prices[idx] < buyInPrice:
                buyInPrice = prices[idx]
            
            maxProfit = max(maxProfit, prices[idx] - buyInPrice)
        return maxProfit
