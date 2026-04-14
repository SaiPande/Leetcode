class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        lst = []
        arr.sort()
        minimum = 9999999
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) < minimum:
                minimum = abs(arr[i+1]-arr[i])

        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) == minimum:
                lst.append([arr[i],arr[i+1]])

        return lst        
