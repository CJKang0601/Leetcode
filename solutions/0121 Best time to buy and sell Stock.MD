```python=
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 100001
        maxprofit = 0
        for price in prices:
            if price < minprice: #在n像裡面做搜索就好 不用考慮雙迴圈
                minprice = price
            
            elif price - minprice > maxprofit: #如果這個不是最小值 就拿來相減
                maxprofit = price - minprice
        
        return maxprofit



```
