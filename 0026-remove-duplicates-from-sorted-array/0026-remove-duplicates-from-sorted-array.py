class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        nums[0] = nums[count]
        count +=1
        while(i<(len(nums)-1)):
            if(nums[i]> nums[i+1]):
                i = i+1   
            elif ((nums[i] != nums[i+1])):
                nums[count] =  nums[i+1]
                count = count + 1   
                i = i + 1
             
            else:
                i = i + 1
        #count = int(count)                 
        return count                
