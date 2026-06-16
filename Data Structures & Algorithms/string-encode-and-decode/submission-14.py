class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # 每個單字後面都強迫黏上一個分隔符 (例如 chr(257))
            res += s + chr(257)
        return res

    def decode(self, s: str) -> List[str]:
        # 如果收到空字串，代表原本是空陣列 []
        if s == "":
            return []
            
        # 用分隔符切開。
        # 注意：因為我們在每個單字後面都加了分隔符，最後切開時尾巴會多出一個空字串
        # 例如 "aābā" 會被切成 ["a", "b", ""]
        # 所以我們用 [:-1] 把最後一個不要的空字串丟掉！
        return s.split(chr(257))[:-1]