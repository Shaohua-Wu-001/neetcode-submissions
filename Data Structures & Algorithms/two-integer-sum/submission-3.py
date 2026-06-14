class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} #老樣子我們用字典去看
        for i, num in enumerate(nums): #把nums的index, 值這些pair都列出來找
            need = target - num  #不直接求解哪兩個數相加等於多少, 反過來求 target-num (i.e.補數)

            if need in seen:
                return [seen[need],i]
            
            seen[num]=i
