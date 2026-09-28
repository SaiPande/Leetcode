class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
                mx = max(mx,cnt)
            if i == ')':
                cnt -=1  
        return mx            