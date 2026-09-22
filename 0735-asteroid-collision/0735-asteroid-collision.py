class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        i = 0
        j = 1

        stack = []

        for i in asteroids:
            flag = True
            while stack:
                if (stack[-1] > 0 and i > 0) or (stack[-1] < 0 and i < 0) or (stack[-1] < 0 and i > 0):
                    break                                      
                else:
                    if abs(stack[-1]) > abs(i):
                        flag = False
                        break

                    elif abs(stack[-1]) < abs(i):
                        stack.pop()
                        continue                                
                    else:
                        stack.pop() 
                        flag = False 
                        break
            if flag:
                stack.append(i)                          
        return stack