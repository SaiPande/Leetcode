class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        max = 0
        for i in range(len(nums)-1):
            if nums[i] == 1 and nums[i+1] == 1:
                count += 1
                if count > max:
                    max = count
            elif nums[i] == 0:
                count = 0
            elif nums[i] == 1 and nums[i+1] == 0:
                count += 1
                if count > max:
                    max = count
                count = 0
        if nums[len(nums)-1] == 1:
            count += 1
            if count > max:
                    max = count
       
        return max
                   