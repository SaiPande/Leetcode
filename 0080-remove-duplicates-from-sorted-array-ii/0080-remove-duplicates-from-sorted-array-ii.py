class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        cnt = 1
        while i<(len(nums)-1):
            if nums[i] == nums[i+1]:
                if cnt<2:
                    cnt += 1
                    i+=1
                else:
                    nums.pop(i+1)
            else:
                cnt = 1 
                i+=1       
        return len(nums)           


