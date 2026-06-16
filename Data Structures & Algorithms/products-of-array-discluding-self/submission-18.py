class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        # 1. 先算前綴積，存入 res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 2. 再算後綴積，直接與 res 相乘
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        # 3. 就得到答案了, 前綴積x後綴積=除了nums[i]本身之外的成積
        return res