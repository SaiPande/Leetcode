class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0]<1:
                return abs(nums[0])+1
            else:
                return 0
        start = 1
        flag = True

        while flag:
            pre = [0]*len(nums)
            
            if start+nums[0] < 1:
                start += 1
                continue
            else: 
                pre[0] = start+nums[0]    
    
            for i in range(1, len(nums)):          
                pre[i] = nums[i] + pre[i-1]
        
                if pre[i] < 1:
                    break    
                if i == (len(nums)-1) and pre[i] > 0:
                    return start     
            start+=1
        return start    