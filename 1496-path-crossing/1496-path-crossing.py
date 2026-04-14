class Solution:
    def isPathCrossing(self, path: str) -> bool:
        lst1 = [(0,0)]
        hori = 0
        verti = 0
        for i in range(len(path)):
            if path[i] == 'N':
                verti += 1
            elif path[i] == 'S':
                verti -= 1
            elif path[i] == 'E':
                hori += 1
            elif path[i] == 'W':
                hori -= 1  

            test = (hori, verti)     
            if test in lst1:   
                return True
            lst1.append((hori, verti))     
                
        if hori == 0 and verti == 0:
                return True        
        return False        
