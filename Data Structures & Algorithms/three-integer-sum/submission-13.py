class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        res = []
        for i in range(n):
            
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            elif i < 0 and sorted_nums[i] == sorted_nums[i + 1]:
                continue

            target = -sorted_nums[i]

            # 這是你固定好 i，算出 target 之後要做的事：
            left = i + 1    # 左邊的人，從 i 的下一格出發
            right = n - 1   # 右邊的人，從最後一格出發

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]
                
                if current_sum == target:
                    # 找到了！這就是你要的組合
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                        
                    # 找到一組後，兩個人同時往內縮，繼續找下一組可能
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    # 太小了！左邊比較輕的人往右走（換大一點的數字）
                    left += 1
                    
                else:
                    # 太大了！右邊比較重的人往左走（換小一點的數字）
                    right -= 1
        return res