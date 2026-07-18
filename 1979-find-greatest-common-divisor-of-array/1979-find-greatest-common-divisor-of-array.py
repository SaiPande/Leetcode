class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minval = min(nums)
        maxval = max(nums)

        return gcd(maxval,minval)