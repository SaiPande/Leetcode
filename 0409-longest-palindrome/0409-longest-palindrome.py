class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1 = {}

        for i in s:
            dict1[i] = dict1.get(i,0)+1
        sum = 0
        isodd = False
        if len(dict1) == 1:
            return list(dict1.values())[0]

        for value in dict1.values():
            if value%2 == 0:
                sum += value
            else: 
                sum += value - 1
                isodd = True 
        if isodd == True:
            sum += 1
        return sum                    