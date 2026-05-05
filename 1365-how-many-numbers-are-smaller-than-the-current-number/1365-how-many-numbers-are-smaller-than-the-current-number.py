class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        outputlist = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count +=1
            outputlist.append(count)

        return outputlist            