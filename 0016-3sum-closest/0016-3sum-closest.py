class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return []
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        mindis = 999999
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1


            while l<r:
                current = nums[l]+nums[r]+nums[i]
                if abs(current-target) < abs(closest-target):
                    closest = current
                if current<target:
                    l+=1
                elif current > target:
                    r-=1
                else:
                    return target        

        return closest 