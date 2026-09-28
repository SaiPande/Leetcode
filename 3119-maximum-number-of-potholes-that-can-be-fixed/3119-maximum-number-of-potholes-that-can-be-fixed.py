class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        lstofconsecutive = []
        cnt = 0
        for i in road:
            if i == 'x':
                cnt +=1
            else:
                if cnt >= budget:
                    #print('here')
                    return budget-1
                else:
                    lstofconsecutive.append(cnt)
                cnt = 0
        if cnt > 0:
            lstofconsecutive.append(cnt)    
        
        lstofconsecutive.sort(reverse= True)
        #print(lstofconsecutive)

        used = 0
        for i in lstofconsecutive:
            if budget <=1:
                break
            if budget>i:
                used += i
                budget = budget-i-1
                
            else:
                used += budget -1
                break
        return used

                