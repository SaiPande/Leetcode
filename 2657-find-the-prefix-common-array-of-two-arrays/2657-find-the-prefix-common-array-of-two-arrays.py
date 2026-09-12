class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freqAB = {}

        output = []

        for i in range(n):
            freqAB[A[i]] = freqAB.get(A[i],0)+1
            freqAB[B[i]] = freqAB.get(B[i],0)+1
            cnt = 0
            for value in freqAB.values():
                if value >= 2:
                    cnt+=1
            output.append(cnt)

        return output            
