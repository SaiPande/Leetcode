class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        stack = [1]
        i=1
        dict1 = set(target)
        while stack and i<=n:
            if len(dict1) == 0:
                return operations
            stack.append(i)    
            operations.append("Push")
            if i in dict1:
                dict1.remove(i)
            else:
                stack.pop()
                operations.append("Pop")
            i+=1    
            print(dict1)    
        return operations        

