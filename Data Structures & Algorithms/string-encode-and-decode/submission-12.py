class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = [] # 因為要回傳陣列呀, 所以需要先做空陣列
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            l = int(s[i:j])

            res.append(s[j+1: j+1+l])
            i = j+1+l
        return res