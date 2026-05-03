class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        t = s
        n = len(s)
        for i in range(n):
            if t == goal:
                return True
            t0 = t[0]    
            t = t[1:n]
            t = t+t0

        return False        