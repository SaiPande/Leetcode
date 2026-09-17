class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        
        n = len(arr)
        
        output = [float('inf')] * n
        
        first = float('inf')  
        second = float('inf') 
        min_len_so_far = float('inf')
        
        i = 0
        j = 0
        sm = 0
        
        while j < n:
            sm += arr[j]
            j += 1
            
            while sm > target and i < j:
                sm -= arr[i]
                i += 1
                
            if sm == target:
                current_len = j - i
                
                if i > 0 and output[i - 1] != float('inf'):
                    if current_len + output[i - 1] < first + second:
                        first = current_len
                        second = output[i - 1]
                
                if current_len < min_len_so_far:
                    min_len_so_far = current_len
                
                sm -= arr[i]
                i += 1
            
            output[j - 1] = min_len_so_far
            
        if first == float('inf') or second == float('inf'):
            return -1
        else:
            return first + second