class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = {} # 就是設立一個空字典 dictionary

        for ch in s:
            count[ch] = count.get(ch,0)+1
            # 如果忘記 .get(ch,0)的函數操作方法, 可以用以下if_else判斷
            # if ch not in count:
            #     count[ch]=1
            # else:
            #     count[ch]+=1
            
        for ch in t:
            if ch not in count:
                return False
            else:
                count[ch]-=1
            if count[ch]<0:
                return False
        return True

