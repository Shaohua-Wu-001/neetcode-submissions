class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(nums) #先變成集合
        longest_streak = 0   # 準備一個計分板，紀錄目前最長的火車有幾節

        for num in num_set:
            # if (num-1) not in num_set:
                head = num
                current_streak = 1

                while (head+1) in num_set:
                    head += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
