class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = []
        k = k1+k2
        for i in range(n):
            diff.append(abs(nums1[i]-nums2[i]))

        if sum(diff)< k:
            return 0
        diff.sort(reverse=True)
        diff.append(0)

        for i in range(1,n+1):
            c = (diff[i-1]-diff[i])*i
            if c > k:
                q, r = divmod(k,i)
                h = diff[i-1]-q
                return (
                    h*h*(i-r)
                    + (h-1)*(h-1)*r
                    + sum(x*x for x in diff[i:n])
                )
            k-=c
        return 0        




        # n = len(nums1)
        # diff = []
        # for i in range(n):
        #     diff.append(abs(nums1[i]-nums2[i]))
    
        # diff.sort(reverse=True)

        # minsum = 0
        # j = 0
        # k = k1+k2
        # if k1 == 0 and k2 == 0:
        #     for i in range(n):
        #         minsum += diff[i]*diff[i]
        #     return minsum
        # else:        
        #     # while k>0 and j<len(diff)-1:
        #     #     if diff[j]>=diff[j+1]:
        #     #         diff[j]-=1
        #     #         k-=1
        #     #     else:
        #     #         j+=1     
        #     #     print(diff)      
        #     # for i in range(n):
        #     #     minsum += diff[i]*diff[i]
        #     # return minsum  

        #     total_diff = sum(diff)
        #     while k > 0 and total_diff > 0: 
        #         if j < len(diff) - 1 and diff[j] > diff[j+1]:
        #             diff[j] -= 1
        #             k -= 1
        #             total_diff -= 1
        #             j = 0
        #         elif j == len(diff) - 1:
        #             diff[j] -= 1
        #             k -= 1
        #             total_diff -= 1
        #             j = 0
        #         else:
        #             j += 1
            
        #     for i in range(n):
        #         minsum += diff[i]*diff[i]
        #     return minsum  