class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MAX = 100001
        pow = [1]*MAX
        
        MOD = 10**9+7

        for i in range(1, MAX):
            pow[i] = (pow[i-1]*10)%MOD

        n = len(s)    
        finalopt = []
        sumoffar, numbersofar, Len = [[0] * (n + 1) for _ in range(3)]

        for i in range(n):
            digit = int(s[i])
            sumoffar[i+1] = sumoffar[i] + digit
            numbersofar[i+1] = (numbersofar[i]*10+digit)%MOD if digit else numbersofar[i]
            Len[i+1] = Len[i] + (digit>0)

        for l,r in queries:
            r+=1

            sub = (numbersofar[l] * pow[Len[r] - Len[l]]) % MOD
            x = (numbersofar[r] - sub) % MOD

            finalopt.append((x * (sumoffar[r] - sumoffar[l])) % MOD)    

        return finalopt    