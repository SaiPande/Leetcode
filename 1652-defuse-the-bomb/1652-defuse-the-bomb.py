class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [element*k for element in code]
        lst1 = [] 
        currentindex = 0  
        lenofcode = len(code)
        count = 0 
        while count < lenofcode:
            
            if k > 0:
                sum = 0
                j = 1
                while j <= k:
                    sum += code[(currentindex+j) % lenofcode]
                    j += 1
                lst1.append(sum)    

            else:
                sum = 0
                j = 1
                while j <= abs(k):
                    sum += code[(currentindex-j) % lenofcode]
                    j+=1 
                lst1.append(sum)       
            currentindex = (currentindex + 1) % lenofcode
            count +=1     
        return lst1    