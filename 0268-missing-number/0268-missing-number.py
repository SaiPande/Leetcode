class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumnum = sum(nums)
        totalsum = int((len(nums)*(len(nums)+1))/2)

        if(totalsum - sumnum)>0:
            return totalsum - sumnum
        elif nums[0] == 0:
            return len(nums)+1 
        else: 
            return 0       