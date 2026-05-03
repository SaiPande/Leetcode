class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        '''
        for i in range(len(arr)):
            if arr[i]*2 in arr[i+1:] or arr[i]/2 in arr[i+1:]:
                return True
        return False        
        '''
        arr.sort()
        for i in range(len(arr)):
            high = len(arr)-1
            low = 0
            target = 2*arr[i]
            while low <= high:
                mid =  (high+low)//2
                if arr[mid]>target:
                    high = mid-1
                elif arr[mid]<target:
                    low = mid + 1
                else:
                    if mid != i:
                        return True 
                    else:
                        if mid + 1 < len(arr) and arr[mid + 1] == target:
                            return True
                        elif mid - 1 >= 0 and arr[mid - 1] == target:
                            return True
                        else:
                            break       
        return False                
                        

