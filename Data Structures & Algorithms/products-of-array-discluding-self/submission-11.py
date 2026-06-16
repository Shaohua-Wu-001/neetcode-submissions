class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            left, right = 1, 1
            for j in range(0,i):
                left *= nums[j]
            for k in range (i+1,n):
                right *= nums[k]
            total = left*right
            res.append(total)
        return res