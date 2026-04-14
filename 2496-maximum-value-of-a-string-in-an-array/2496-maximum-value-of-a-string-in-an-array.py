class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxval = 0
        for i in range(len(strs)):
            count = 0
            if strs[i].isdigit() == True:
                for j in range(len(strs[i])):
                    if strs[i][j] == 0:
                        continue
                    else: 
                        nums = strs[i][j:]
                        break       
                count = int(nums)
                if maxval < count:
                    maxval = count  
            else:
                count = len(strs[i])
                if maxval < int(count):
                    maxval = count          
        return maxval                