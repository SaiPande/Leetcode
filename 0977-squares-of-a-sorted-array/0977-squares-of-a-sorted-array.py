class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        sortedlst = [0]*len(nums)
        p = len(nums) - 1  

        while l<=r:
            if nums[l]*nums[l] > nums[r]*nums[r]:
                sortedlst[p] = nums[l]*nums[l]
                l+=1
            else:
                sortedlst[p] = nums[r]*nums[r]
                r-=1
            p-=1    

        return sortedlst              