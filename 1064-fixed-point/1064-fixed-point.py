class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        l,r = 0, len(arr)-1
        ans = -1

        while l<=r:
            mid = l + (r-l)//2

            if arr[mid] == mid:
                ans = mid      
                r = mid - 1    
            elif arr[mid] < mid:
                l = mid + 1    
            else:
                r = mid - 1    
        return ans        
                       
        # for i,num in enumerate(arr):
        #     if i==num:
        #         return i
        # return -1        