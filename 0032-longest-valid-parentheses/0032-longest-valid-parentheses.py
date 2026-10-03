class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        maxvalparentheses = 0
        stk = []
        stk.append(-1)

        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)    
                else:
                    maxvalparentheses = max(maxvalparentheses, i-stk[-1])

        return maxvalparentheses



        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # ans = [0,0]

        # def validpalindrome(s1:str)->Boolean:
        #     stk = []

        #     for i in s1:
        #         if i == '(':
        #             stk.append(i)
        #         elif i == ')':
        #             if stk[-1] == '(': 
        #                 stk.pop()
        #             else:
        #                 stk.append(i)   
        #     if stk:
        #         return False
        #     return True                 

        # for i in range(n-1):
        #     if s[i] == '(' and s[i+1] == ')':
        #         dp[i][i+1] = True
        #         ans = [i, i+1]

        # for diff in range(2,n):
        #     for i in range(n-diff):
        #         j = i+diff
        #         if s[i] == '(' and s[j] == ')' and dp[i+1][j-1]:
        #             dp[i][j] = True
        #             ans = [i,j]
        # print(dp)
        # print(ans)
        # i,j = ans
        # return s[i:j+1]     