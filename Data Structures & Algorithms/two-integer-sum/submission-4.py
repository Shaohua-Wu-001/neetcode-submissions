class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} #老樣子我們用字典去看
        for i, num in enumerate(nums): #把nums的index, 值這些pair都列出來找
            need = target - num  #不直接求解哪兩個數相加等於多少, 反過來求 target-num (i.e.補數)

            if need in seen:
                return [seen[need],i]
            
            seen[num]=i

# 解釋一下
# 我從左到右看 nums。

# 每看到一個數 num，
# 我先算出它需要誰 need。

# 如果 need 以前出現過，
# 那 need 的位置 + 現在 num 的位置 就是答案。

# 如果 need 沒出現過，
# 那我就把現在這個 num 記起來，
# 讓後面的人可以找它。