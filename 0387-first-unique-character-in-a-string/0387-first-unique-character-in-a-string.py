class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else: 
                dict[i] = 1

        for key, value in dict.items():
            if value == 1:
                return s.index(key)

        return -1