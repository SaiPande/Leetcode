class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        lst = []
        dict1 = {}
        for i in words:
            lst.append(tuple(sorted(set(i))))

        for i in lst:
            dict1[i] = dict1.get(i,0) + 1
        print(dict1)
        count = 0
        for val in dict1.values():
            if val > 1:
                count += val * (val - 1) // 2
        return count        