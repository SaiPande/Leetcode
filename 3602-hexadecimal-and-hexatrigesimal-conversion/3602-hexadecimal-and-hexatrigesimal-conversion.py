class Solution:
    def concatHex36(self, n: int) -> str:
        n2 = n*n
        n3 = n*n*n
        alpha = {i-55: chr(i) for i in range(65,91)}
        hexa = ''
        hexat = ''
        i = n2
        while(i >0):           
            rem = i%16
            if rem >= 10:
                hexa += alpha[rem]
            else: 
                hexa += str(rem)
            i = i//16    
               
        i = n3
        while(i >0):       
            rem = i%36
            if rem >= 10:
                hexat += alpha[rem]  
            else: 
                hexat += str(rem)      
            i = i//36
        
        return hexa[::-1]+hexat[::-1]