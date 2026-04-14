class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count_sum = 0
        output = []
        for i in range(len(nums)):
            count_sum += nums[i]
            output.append(count_sum)
        return output    