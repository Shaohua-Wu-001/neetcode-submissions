from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count={}

        for ch in s:
            count[ch] = count.get(ch,0)+1 #計算是否出現在s中的字母是有在字典內的, 沒有的話就設定為0開始, 第一次就+1.
        
        for ch in t:
            if ch not in count:
                return False
            else:
                count[ch]-=1
            if count[ch] < 0:
                return False
        return True