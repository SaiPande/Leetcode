class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for i in s:
            freq[i] = freq.get(i,0)+1
        
        maxodd = 0
        mineven = 99999

        for key, value in freq.items():
            if value%2 == 1 and value > maxodd:
                maxodd = value
            if value%2 == 0 and value < mineven:
                mineven = value

        return maxodd - mineven  
        