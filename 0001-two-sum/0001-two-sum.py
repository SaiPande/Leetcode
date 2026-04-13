class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputlist = []
        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)):
                if ((nums[i] + nums[j]) == target and (i != j)):
                    outputlist.append(i)
                    outputlist.append(j)
                    return outputlist