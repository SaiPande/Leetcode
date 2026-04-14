class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack1 = []

        i = 0
        j = 0
        while i < len(pushed) and j < len(popped): 
            if stack1: 
                if stack1[-1] != popped[j]:
                    stack1.append(pushed[i])
                    i += 1
                else:
                    stack1.pop()
                    j += 1
            else: 
                stack1.append(pushed[i])
                i += 1
        
        while stack1:
            if stack1[-1] == popped[j]:
                stack1.pop()
                j += 1
            else:
                return False
        return True                    



                    
