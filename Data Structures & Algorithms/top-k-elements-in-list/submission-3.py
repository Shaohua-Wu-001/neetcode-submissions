class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        ans = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans