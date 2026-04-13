class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        dict = {}

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for key, val in dict.items():
            print(val)
            if val < 2:
                continue
            isprime = True
            for i in range (2, val):  
                if val % i == 0:
                    isprime = False
                    break

            if isprime:
                return True
            
        return False

    