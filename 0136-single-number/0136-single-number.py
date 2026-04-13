class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        i = 1
        j = 2
        k = 0
        count = 0
        if len(nums)>1:
            while (i < len(nums)-1) :           
                if nums[k] != nums[i] and k == 0:
                        return nums[k] 
                    #count+ = 1
                elif nums[i] != nums [j] and j == (len(nums)-1): 
                        return nums[j]
                elif nums[k] != nums[i] and  nums[i] != nums [j]: 
                    return nums[i]              
                i+=1
                j+=1
                k+=1 
        else:
            return nums[0]           
            
