class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} #基本上很老套, 你還是需要建立字典
        for word in strs:
            count = [0]*26
            for ch in word:
                index = ord(ch) - ord('a')
                count[index]+=1

            key = tuple(count) #注意這邊key不能是list, 可以是tuple!
                               # 因為 dictionary 的 key 必須是：不可變，而且可以被 hash 的東西
            if key not in group:
                group[key]=[]
            
            group[key].append(word)
        return list(group.values())
                