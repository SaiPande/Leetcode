class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxval = max(nums)
        output = 0
        for i in nums:
            if i<maxval:
                output += (maxval-i)

        return output        