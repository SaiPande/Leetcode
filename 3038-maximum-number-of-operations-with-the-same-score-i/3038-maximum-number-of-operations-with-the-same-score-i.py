class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        s12 = nums[0]+nums[1]
        nums = nums[2:]
        count = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] + nums[i+1] == s12:
                count += 1
                i+=2
            else:
                break
        return count        