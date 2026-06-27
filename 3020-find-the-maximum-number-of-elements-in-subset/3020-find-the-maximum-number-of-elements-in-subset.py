class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxchainlength = {}
        #seensqrt = set()
        maxval = 1
        if 1 in counts:
            ones_count = counts[1]
            maxval = ones_count if ones_count % 2 != 0 else ones_count - 1

        for i in range(len(nums)):   
            t = nums[i]
            if t == 1:
                continue
            else:
                cnt = 0
                sqrtnum = int(math.sqrt(t))
                if sqrtnum * sqrtnum != t:
                    continue
                while sqrtnum>0:
                    if sqrtnum == 1:
                        break
                    if counts[sqrtnum]>1:
                        cnt+=2
                    else:
                        break    
                    
                    next_sqrt = int(math.sqrt(sqrtnum))
                    if next_sqrt * next_sqrt != sqrtnum:
                        break
                    sqrtnum = next_sqrt
                
                if cnt > 0:
                    maxval = max(cnt+1,maxval) 

                #seensqrt.add(t)       
        return maxval             
                      