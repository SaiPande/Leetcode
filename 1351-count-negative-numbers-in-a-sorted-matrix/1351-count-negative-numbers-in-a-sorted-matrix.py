class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        cnt = 0
        target = 0

        for i in grid:

            low = len(i)-1
            high = 0
            idx = -1
            while high<=low:
                mid = high + ((low-high)//2)

                if i[mid] < target:
                    idx = mid
                    low = mid -1
                else:
                    high = mid +1
            if i[idx] >=0:
                cnt+=0
            else:
                cnt+= len(i[idx:])

        return cnt    