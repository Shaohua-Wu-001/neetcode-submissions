class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        items = count.items() #就是要把字典都列出來(keys,values)
        
        #接下來要對values排序, 最後列出keys為何?
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True) #True是由小到大
        
        #最後是把最大的values對應之keys列出
        ans = [] 
        for item in sorted_items[:k]: #前k個最常出現的
            ans.append(item[0]) #把keys回傳就好

        return ans #最後的答案啦