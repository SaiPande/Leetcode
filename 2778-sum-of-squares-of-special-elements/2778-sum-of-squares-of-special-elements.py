class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumsqr = 0
        n = len(nums)
        for i in range(n):
            if n%(i+1) == 0:
                sumsqr+= (nums[i]*nums[i])
        return sumsqr        