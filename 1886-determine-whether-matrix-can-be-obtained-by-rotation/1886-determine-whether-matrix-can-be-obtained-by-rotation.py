class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        count = 4
        while count >0:
            for i in range(len(mat)):
                for j in range(0,i):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            for i in range(len(mat)):
                mat[i] = mat[i][::-1]        
            if mat == target:
                return True
            count -=1    
        return False       
