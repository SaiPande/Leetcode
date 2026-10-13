class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]

        nums.sort()

        return -sum(nums[:n//2])+sum(nums[n//2:])
        # i = 0
        # j = len(nums)-1
        # maxval = 0
        # while i<j:
        #     maxval += (nums[j]-nums[i])
        #     i+=1
        #     j-=1

        # if len(nums)%2 == 1:
        #     maxval+=nums[i]

        # return maxval    

