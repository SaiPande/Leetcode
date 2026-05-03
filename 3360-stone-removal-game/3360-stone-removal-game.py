class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        count = 10

        while n-count >= 0:
            n -= count
            count -= 1 
            turn += 1

        return turn%2 == 1