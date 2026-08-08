class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = [0,0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]

        for diff in range(2,n):
            for i in range(n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]

        i,j = ans
        return s[i:j+1]                       

        # n = len(s)
        # if n==1:
        #     return s
        # i = 0
        # j = n-1
        # paliset = set()
        # while i<=j:
        #     if s[i] == s[j]:
        #         k = i
        #         l = j
        #         while k < l and s[k] == s[l]:
        #             k += 1
        #             l -= 1
        #             if k>=l:
        #                 paliset.add(s[i:j+1])       
        #     if i < j:
        #         j -= 1
        #     else:
        #         i += 1
        #         j = n - 1
        # return max(paliset, key=len, default=s[0])



        