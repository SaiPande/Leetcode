class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            binary = (bin(i)[2:])
            lst.append(binary.count('1'))

        return lst 