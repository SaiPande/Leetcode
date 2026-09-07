class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        my_lists = [""]*numRows
        idx = 0
        forward = True
        for i in s:
            my_lists[idx] += i
            if idx == (numRows-1):
                forward = -1
            elif idx == 0:
                forward = 1 
            
            idx += forward    
        
        return "".join(my_lists)




