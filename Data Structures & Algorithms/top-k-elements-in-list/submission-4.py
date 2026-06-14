class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # 用 bucket algorithm
        # bucket 在這邊為出現的頻率

        bucket = [[] for _ in range(len(nums) + 1)] #建立出頻率的bucket, 都是空字串!

        for num, freq in count.items():
            bucket[freq].append(num) #放到對應頻率的bucket中

        ans = []

        for freq in range(len(bucket) - 1, 0, -1): #由大到小
            for num in bucket[freq]:
                ans.append(num)
                if len(ans) == k: #前k個
                    return ans