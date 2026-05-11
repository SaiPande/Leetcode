class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # pref = [0]*n
        # suff = [0]*n
        # output = [0]*n
        
        # pref[0] = suff[n-1] = 1

        # for i in range(1,n):
        #     pref[i] = nums[i-1]*pref[i-1]
        # for i in range(n-2, -1, -1):
        #     suff[i] = nums[i+1]*suff[i+1]
        # for i in range(n):
        #     output[i] = pref[i]*suff[i]            

        # return output 

        #_______________________________

        zeroindex = [] 
        optlst = []
        lst = [0]*len(nums)
        total = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroindex.append(i)
            else: 
                total *= nums[i]
        if len(zeroindex)>1:
            return lst
        else:
            if len(zeroindex) == 1:    
                lst[zeroindex[0]] = total
                return lst
            else:
                for i in range(len(nums)):
                    lst[i] = total//nums[i]
        return lst                



