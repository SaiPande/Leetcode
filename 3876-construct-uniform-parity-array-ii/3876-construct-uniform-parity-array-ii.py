class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimumnum = nums1[0]
        hasOddnum = False

        for i in nums1:
            if i<minimumnum:
                minimumnum = i
            if i & 1:
                hasOddnum = True
        print(minimumnum)    
        if minimumnum & 1:
            return True
        return not hasOddnum                
                    

