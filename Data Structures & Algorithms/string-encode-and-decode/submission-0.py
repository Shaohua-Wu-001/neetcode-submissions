class Solution:
    def encode(self, strs: List[str]) -> str:
        res = "" # 先準備一個空字串
        for s in strs:
            # 每個字串前面加上「長度+#」
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # 因為要回傳陣列, 因此要設立空陣列><
        
        while i < len(s):
            # 找下一個 '#' 的位置
            j = i
            while s[j] != "#":
                j += 1
            
            # i 到 j 之間就是長度的數字
            length = int(s[i:j])
            
            # 根據長度，精準抓取字串
            # j+1 是字串開始的地方，j+1+length 是字串結束的地方
            res.append(s[j+1 : j+1+length])
            
            # 把指針移動到下一個字串的開頭
            i = j + 1 + length
            
        return res