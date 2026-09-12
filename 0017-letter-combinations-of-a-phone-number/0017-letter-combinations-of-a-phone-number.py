class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return []

        def backtracking(idx, path):
            if len(path) == len(digits):
                output.append("".join(path))
                return 

            combi = dict1[digits[idx]]

            for p in combi:
                path.append(p)
                backtracking(idx+1, path)
                path.pop()

        output = []
        backtracking(0,[])
        return output
                    
            