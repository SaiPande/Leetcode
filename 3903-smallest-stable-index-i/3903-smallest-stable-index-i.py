class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        #tmax = max(nums)
        for i in range(len(nums)):
            t = max(nums[0:i+1])
            if (t - min(nums[i:])) <= k:
                return i
        return -1        