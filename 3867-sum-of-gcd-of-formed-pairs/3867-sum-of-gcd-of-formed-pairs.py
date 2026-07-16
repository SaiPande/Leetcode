class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxofi, n = 0, len(nums)

        for i in range(n):
            maxofi = max(maxofi, nums[i])
            nums[i] = gcd(nums[i], maxofi)

        nums.sort()

        return sum(gcd(nums[i], nums[~i]) for i in range(n//2))        