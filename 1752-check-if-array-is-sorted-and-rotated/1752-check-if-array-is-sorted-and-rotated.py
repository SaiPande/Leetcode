class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 0 
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag = 1
                break
        if flag == 1:
            nums = nums[i+1:]+nums[0:i+1]    
        else:
            return True    

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False 
        return True  