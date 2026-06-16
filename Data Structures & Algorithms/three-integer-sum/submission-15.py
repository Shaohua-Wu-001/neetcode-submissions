class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        res = []
        for i in range(n):

            # 1. 移項得到目標值
            target = -sorted_nums[i]
            
            # 2. 很重要的是 事先在外部要避免重複!
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]: 
                continue

            left = i + 1
            right = n - 1 

            # 3. 使用 Two pointer 解法
            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]
                
                if current_sum == target:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    
                    # 4. 很重要的是內部也要避免重複!
                    # --> "左邊往右一格 or 右邊往左一格" > 避免重新計算一樣的值!!
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                        
                    # 5. 找到一組後，兩個人同時往內縮，繼續找下一組可能
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    # 左邊比較輕的人往右走（換大一點的數字）
                    left += 1   
                else:
                    # 右邊比較重的人往左走（換小一點的數字）
                    right -= 1
        return res