class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        dash = 0
        if len(moves) == 0:
            return 0
        for i in moves:
            if i == 'L':
                left+=1
            elif i == 'R':
                right+=1 
            else:
                dash+=1 

        if left > right:
            return left-right+dash
        elif right > left:
            return right-left+dash
        else:
            return dash                          
