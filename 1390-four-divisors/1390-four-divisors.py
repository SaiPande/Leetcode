class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        maxval = 0
        for i in nums:
            j = 1
            sumnum = 0
            count = 0
            while j <= math.sqrt(i):
                if i%j == 0:
                    print(j)
                    sumnum+=j
                    count+=1
                    if j != i // j:
                        sumnum += i // j
                        count += 1
                if count>4:
                    break
                j+=1  
            if count == 4:
                maxval += sumnum      
        return maxval        