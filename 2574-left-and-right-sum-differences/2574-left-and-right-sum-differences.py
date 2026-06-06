class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [0]*len(nums)
        rightsum = [0]*len(nums)
        leftsum[0] = nums[0]
        for i in range(1,n):
            leftsum[i] = nums[i] + leftsum[i-1]

        rightsum[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            rightsum[i] = nums[i] + rightsum[i+1]  
        optlist = []
        for i in range(n):
            optlist.append(abs(leftsum[i]-rightsum[i]))
        return optlist    