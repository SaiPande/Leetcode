class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        if len(arr)<3:
            return []
        arr.sort()
        count = 0
        mod = 10**9+7

        for i in range(len(arr)-2):
            l = i+1
            r = len(arr)-1

            while l<r:
                if arr[l]+arr[r]+arr[i] < target:
                    l+=1
                elif arr[l]+arr[r]+arr[i] > target:
                    r-=1
                else:

                    if arr[l] == arr[r]:
                        elements = r - l + 1
                        count += (elements * (elements - 1)) // 2
                        break
                        
                    leftcnt = 1
                    rightcnt = 1
                    while l<r and arr[l] == arr[l+1]:
                        leftcnt+=1
                        l+=1
                    while l<=r and arr[r] == arr[r-1]:
                        rightcnt+=1
                        r-=1    
                    count += leftcnt * rightcnt
                    l+=1
                    r-=1
        return count%mod            
