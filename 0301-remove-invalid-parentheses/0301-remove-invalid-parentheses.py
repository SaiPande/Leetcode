class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        #####   NEED TO REVISIT AS I WANST ABLE TO SOLVE THIS ON MY OWN OR EVEN GOT ANY INTUITION FOR THIS CODE 

        output = []

        stack = [(s, 0, 0, ('(',')'))]

        while stack:
            current, left, right, par = stack.pop()

            n = len(current)

            bal = 0

            match = False

            for i in range(left, n):
                bal += ((current[i] == par[0]) - (current[i] == par[1]))
                print(bal)

                if bal>= 0:
                    continue


                for j in range(right, i+1):
                    if (current[j] == par[1]) and (j == right or current[j-1] != par[1]):
                        next = current[:j] + current[j+1:]
                        stack.append((next, i,j, par))

                match = True
                break        

            if not match:
                rev = current[::-1]

                if par[0] == "(":
                    stack.append((rev, 0, 0, (")", "(")))
                else:
                    output.append(rev)

        return output