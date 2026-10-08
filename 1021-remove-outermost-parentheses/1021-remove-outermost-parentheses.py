class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #stk = []
        output = []
        start = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt +=1
            else:
                if cnt > 0:
                    cnt -= 1
                    if cnt == 0:
                        output.append(s[start+1:i])
                        start = i+1
        return ''.join(output)                                