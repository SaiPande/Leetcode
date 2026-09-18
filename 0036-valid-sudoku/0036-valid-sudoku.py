class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        rset = [set() for i in range(n)]
        cset = [set() for i in range(n)]
        bset = [set() for i in range(n)] 

        for r in range(n):
            for c in range(n):

                v = board[r][c]

                if v == ".":
                    continue

                if v in rset[r]:
                    return False
                rset[r].add(v)

                if v in cset[c]:
                    return False
                cset[c].add(v)

                boxcal = (r//3)*3 + c//3

                if v in bset[boxcal]:
                    return False
                bset[boxcal].add(v)    

        return True        