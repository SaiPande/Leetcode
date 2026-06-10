class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxval = 0

        for i,jump in enumerate(nums):

            if i>maxval:
                return False

            maxval = max(maxval, i+jump)

            if maxval> len(nums)-1:
                return True           

        return True        