class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0:
            return [""]

        paranthesislist = []

        for i in range(n):
            leftstr = self.generateParenthesis(i)
            rightstr = self.generateParenthesis(n-1-i)

            for j in leftstr:
                for k in rightstr:
                    paranthesislist.append("("+j+")"+k)

        return paranthesislist