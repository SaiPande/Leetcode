class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = 0
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        lst = list(dict.items())
        lst.sort()
        for i in range(0, len(lst) - 1):
            (key1, val1) = lst[i]
            (key2, val2) = lst[i + 1]

            if key2 - key1 == 1:
                if (val1+val2) > count:
                    count = val1 + val2

        return count            

