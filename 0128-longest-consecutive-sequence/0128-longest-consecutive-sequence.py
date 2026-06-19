class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums or len(nums) <1:
        #     return 0
        # elif len(nums) == 1:
        #     return 1   
        maxval = 0
        count = 0
        s1 = set(nums)          # use set, avoid checking for repeat numbers
        for i in s1:
            if (i - 1) not in s1:        # check if prev num is not there, because anyways we will calculate for that and it will be longer conq seq
                nextnum = i
                while nextnum in s1:
                    count += 1
                    nextnum += 1
                else:
                    maxval = max(maxval, count)
                    count = 0
                    
        return maxval         
        
        
        # if not nums or len(nums) <1:
        #     return 0
        # elif len(nums) == 1:
        #     return 1   
        # maxval = max(nums)
        # minval = min(nums)
        # maxseq = 0
        # count = 0
        # output = [float('inf')] * (maxval - minval + 1)

        # for i in nums:
        #     output[i - minval] = i
        # for num in output:
        #     if num != float('inf'):
        #         count+=1
        #     else:
        #         maxseq = max(maxseq, count)
        #         count = 0 
        # maxseq = max(maxseq, count)        
        # return maxseq           