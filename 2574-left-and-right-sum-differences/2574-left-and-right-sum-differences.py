class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return lst 