class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minval = min(nums)
        maxval = max(nums)
        gcdval = 0
        for i in range(1, minval+1):
            if minval%i == 0 and maxval%i == 0:
                gcdval = i
        return gcdval    