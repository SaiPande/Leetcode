class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i,0)+1

        for key, val in dict1.items():
            if val == n:
                return key