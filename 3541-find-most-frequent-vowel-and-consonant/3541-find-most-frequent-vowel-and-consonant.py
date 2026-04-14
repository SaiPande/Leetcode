class Solution:
    def maxFreqSum(self, s: str) -> int:
        dict1 = {}
        dict2 = {}
        for i in s:
            if i in 'aeiou':
                dict1[i] = dict1.get(i, 0) + 1
       
        for i in s:
            if i not in 'aeiou':
                dict2[i] = dict2.get(i, 0) + 1

        max1 = max(dict1.values()) if dict1 else 0
        max2 = max(dict2.values()) if dict2 else 0
        return max1 + max2
