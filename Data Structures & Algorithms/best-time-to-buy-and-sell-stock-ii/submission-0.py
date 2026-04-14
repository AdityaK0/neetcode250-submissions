class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        previous_price = prices[0]

        for i in range(1,len(prices)):
            if prices[i]<previous_price:
                # then sell the previous price stock on the same day
                # and update the previous_price i.e again by at low
                previous_price = prices[i]
            else:
                profit+=prices[i]-previous_price
                previous_price = prices[i]

        return profit        

        