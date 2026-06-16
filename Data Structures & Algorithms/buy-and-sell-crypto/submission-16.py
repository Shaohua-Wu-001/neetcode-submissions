class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 這題會是希望用 dynamic programming 進行解題喔：
        maxP = 0 #最大獲利
        minBuy = prices[0] #最低買價

        # 設每天都要賣
        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        
        # n = len(prices)
        # max_profit = 0
        # left, right = 0, 1

        # while right < n:
        #     # 如果發現右邊（賣出）比左邊（買入）高，代表有賺頭！
        #     if prices[left] < prices[right]:
        #         curr_profit = prices[right] - prices[left]
        #         max_profit = max(max_profit, curr_profit)
        #     else:
        #         # 關鍵：如果右邊的價格居然比左邊還要低！
        #         # 代表找到了「更便宜的買入點」，立刻把 left 移過來
        #         left = right
        #     # 不管有沒有賺錢，右指針每天都要繼續往後看
        #     right += 1
            
        # return max_profit