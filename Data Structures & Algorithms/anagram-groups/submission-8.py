class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} #基本上很老套, 你還是需要建立字典
        for word in strs:
            key = ''.join(sorted(word))
            #只是這次你不能只是sorted(.)因為這樣出來是list 
            #例如說你的act會變成[]'a','c','t'], 所以需要''.join變成一個str字串
            if key not in group:
                group[key]= [] #這邊是去字典 group 裡面，找 key 對應的 value, 如果目前沒有的話就要給他空字串啊
            group[key].append(word)
        return list(group.values())
