class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        nums.sort()
        count = 0

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l<r:
                if nums[l]+nums[r]+nums[i] < target:
                    count+=r-l
                    l+=1
                else:
                    r-=1       
        return count            