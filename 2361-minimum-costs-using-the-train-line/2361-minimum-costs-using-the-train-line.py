class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)
        lst = []
        reg_cost = 0
        exp_cost = expressCost

        for i in range(n):

            next_reg = min(reg_cost + regular[i], exp_cost + regular[i])
            next_exp = min(exp_cost + express[i], reg_cost + expressCost + express[i])

            reg_cost = next_reg
            exp_cost = next_exp

            lst.append(min(reg_cost, exp_cost))
        return lst    
        
        # Greedy approach doesnt work here!!! Need to think of the previous steps and the next steps!!!
        # mincost = 0
        # n = len(regular)
        # lst = []
        # expressway = False
        # for i in range(n):
        #     if expressway:  # express way
        #         if regular[i] < express[i]:
        #             mincost += regular[i]
        #             expressway = False   
        #         else:
        #             mincost += express[i]   

        #     else:    # not Express way 
        #         if regular[i] <= (express[i]+expressCost):
        #             mincost+= regular[i]        
        #         elif regular[i] > (express[i]+expressCost):
        #             t = express[i]+expressCost
        #             mincost += t
        #             expressway = True

        #     lst.append(mincost)
        # return lst            