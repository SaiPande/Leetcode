from typing import List

class Practice66:
    def pikori(self, digits:List[int])-> List[int]:
        count = len(digits)
        i = 1
        num = 0
        while(i <= count):
            if digits[count-i] == 9:
                num+=1
            else : 
                break
            i+=1    
        
        if num == count: 
            for i in range(len(digits)): 
                if i == 0:
                    digits[i] = 1
                else :
                    digits[i] = 0    
            digits.append(0)    

        elif num < count and num > 0: 
            j = 0
            while(j < num):
                digits[count-1-j] = 0
                if j == num-1:
                    digits[count-1-num] = digits[count-1-num]+1
                j+=1
            #digits.append(0)
        elif digits[len(digits) - 1] < 9:
            digits[len(digits) - 1] = digits[len(digits) - 1] + 1        



        print(digits)           
        return digits  
    
if __name__ == "__main__" : 
    obj = Practice66()
    test = obj.pikori([9,9,9])