class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
        '''dict = {}
        vert = 0
        hori = 0
        for i in moves:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        print(dict)
        
        vert = dict.get('U', 0) - dict.get('D', 0)
        hori = dict.get('L', 0) - dict.get('R', 0)      
        if vert == 0 and hori == 0:
            return True
        else:
            return False         
        '''    