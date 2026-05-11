class Solution:
    def compress(self, chars: List[str]) -> int:
        # dict1 = {}
        # for i in chars:
        #     dict1[i] = dict1.get(i,0)+1

        # result = []
        # for key,value in dict1.items():
        #     result.append(key)
        #     result.append(str(value))
        #     print(result)
        # return len(result) 
        

        if len(chars) < 1:
            return chars
        
        count = 1
        i = 1
        j = 0
        while i < len(chars):
            if chars[i] == chars[i-1]:
                count +=1
            else:
                if count == 1:
                    chars[j] = chars[i-1]
                    j+=1
                else:    
                    chars[j] = chars[i-1]
                    for digit in str(count):
                        chars[j+1]= digit
                        j+=1
                    j+=1
                count = 1    
            i+=1
        if count == 1:
            chars[j] = chars[i-1]
            j+=1
        else:    
            chars[j] = chars[i-1]
            for digit in str(count):
                chars[j+1]= digit
                j+=1
            j+=1

        return j    

