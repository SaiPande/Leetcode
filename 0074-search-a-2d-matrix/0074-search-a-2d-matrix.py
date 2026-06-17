class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        h = len(matrix)-1
        collen = len(matrix[0])
        while l<=h:
            mid = l + (h-l)//2

            if target > matrix[mid][-1]:
                l = mid+1
            elif target < matrix[mid][0]:
                h = mid -1
            else:
                break    

        if not (l<=h):
            return False
        row = mid
        lcol = 0
        hcol = collen-1
        while lcol<=hcol:
            mid = lcol + (hcol-lcol)//2
            if target > matrix[row][mid]:
                lcol = mid+1
            elif target < matrix[row][mid]:
                hcol = mid -1
            else:
                return True    
        return False        
