Problem Description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
![image](https://user-images.githubusercontent.com/11685096/151922532-a9862f49-b693-4dac-bef4-1d1899fbed79.png)

Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit= 0
        min_profit = prices[0]
        for i in range(1, len(prices)):
            min_profit = min(min_profit, prices[i])
            if prices[i] > min_profit: 
                profit = prices[i] - min_profit
                maxprofit = max(maxprofit, profit)
        return maxprofit
```
