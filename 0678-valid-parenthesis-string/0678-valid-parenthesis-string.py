class Solution:
    def checkValidString(self, s: str) -> bool:
        #Need to be careful with the positions when valid parenthesis
        stk = []
        star_stk = []
        starcnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)    
            elif s[i] == ')':
                if stk:
                    stk.pop()
                elif star_stk:
                    star_stk.pop()
                else:
                    return False
            else:
                star_stk.append(i)            

        while stk and star_stk:
            if star_stk[-1]<stk[-1]:   #when the index of star is less than the opening backet index -> invalid
                return False
            stk.pop()
            star_stk.pop()
        
        return len(stk) == 0
        
        #Failed because I didnt take into consideration if stars are before and the only thing remaining are opening brackets and visa versa!!!! 
        # stk = []
        # starcnt = 0
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         stk.append(s[i])
        #     elif s[i] == ')':
        #         if stk and stk[-1] == '(':
        #             stk.pop()
        #         else:
        #             stk.append(s[i])
        #     else:
        #         starcnt += 1
        # print(stk) 
        # print(starcnt)       
        # if stk:
        #     if starcnt - len(stk)>=0:
        #         return True
        #     else:
        #         return False         
        # return True                    