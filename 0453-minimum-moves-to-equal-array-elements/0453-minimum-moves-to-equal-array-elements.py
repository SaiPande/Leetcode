class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        output = 0

        for i in range(len(nums)-1, -1, -1):
            output += nums[i] - nums[0]

        return output    