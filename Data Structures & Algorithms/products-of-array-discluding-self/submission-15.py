class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 方法一：在每一次計算 res[i] 時，都會重新跑兩次迴圈去算左邊和右邊的乘積。
        # 如果陣列長度是 N，你需要計算 N×N 次，時間複雜度是 O(N^2)
        # n = len(nums)
        # res = []
        # for i in range(n):
        #     left, right = 1, 1
        #     for j in range(0,i):
        #         left *= nums[j]
        #     for k in range (i+1,n):
        #         right *= nums[k]
        #     total = left*right
        #     res.append(total)
        # return res

        # 方法二：最佳解 (prefix -> 前綴*後綴)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
            
        # 1. 先算前綴積，存入 res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
                
            # 2. 再算後綴積，直接與 res 相乘
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]   
        return res



