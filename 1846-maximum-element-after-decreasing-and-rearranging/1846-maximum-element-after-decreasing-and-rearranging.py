class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr)<1:
            return 0
        
        arr.sort()
        arr[0] = 1

        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1]+1)

        return arr[-1]  

