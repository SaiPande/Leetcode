class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i< n:
            if arr[i] == 0:
                cnt = 0
                j = i
                while j < len(arr) and arr[j] == 0:
                    cnt+=1
                    j+=1
                
                for k in range(cnt):
                    arr.insert(j, 0)
                i = j+cnt+1
            else: 
                i += 1

        arr[:] = arr[:n]